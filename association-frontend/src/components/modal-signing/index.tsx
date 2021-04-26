import React, { useState } from "react";
import { useFormState } from "react-use-form-state";

import { Alert, Variant } from "~/components/alert";
import { Button } from "~/components/button";
import { Input } from "~/components/input";
import { Modal } from "~/components/modal";
import { getMessageForError, isErrorTypename } from "~/helpers/errors-to-text";

import { useLoginMutation } from "./login.generated";
import { useRegisterMutation } from "./register.generated";

type ModalSigningProps = {
  showModal: boolean;
  closeModalHandler?: () => void;
};

type SigningForm = {
  email: string;
  password: string;
};

export const ModalSigning: React.FC<ModalSigningProps> = ({
  showModal,
  closeModalHandler,
}) => {
  const [formState, { email, password }] = useFormState<SigningForm>();
  // login or signup
  const [isLoggingIn, setIsLoggingIn] = useState(false);
  const [loginData, login] = useLoginMutation();
  const [registerData, register] = useRegisterMutation();

  const submitLogin = async () => {
    const result = await login({
      input: {
        email: formState.values.email,
        password: formState.values.password,
      },
    });

    if (result.data.login.__typename === "LoginSuccess") {
      window.dispatchEvent(new Event("userLoggedIn"));
      closeModalHandler();
    }
  };

  const submitRegister = async () => {
    const result = await register({
      input: {
        email: formState.values.email,
        password: formState.values.password,
      },
    });

    if (result.data.register.__typename === "RegisterSuccess") {
      console.log("register success!");
      window.dispatchEvent(new Event("userLoggedIn"));
      closeModalHandler();
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isLoggingIn) {
      submitLogin();
    } else {
      submitRegister();
    }
  };

  const isRunningMutation = loginData.fetching || registerData.fetching;
  const mutationData = isLoggingIn
    ? loginData.data?.login
    : registerData.data?.register;
  const mutationResultTypename = mutationData?.__typename;
  const operationFailed = isErrorTypename(mutationResultTypename);

  return (
    <Modal
      className="items-center"
      showModal={showModal}
      closeModalHandler={closeModalHandler}
      title={
        isLoggingIn
          ? "Accedi al tuo account Python Italia"
          : "Entra nella community di Python Italia"
      }
    >
      <form className="flex flex-col max-w-sm mx-auto" onSubmit={handleSubmit}>
        <div className="flex flex-col mb-5">
          <Input required placeholder="Email" {...email("email")} />
          <div className="place-self-start">
            <a
              href="#"
              className="block mt-1 underline text-bluecyan hover:text-yellow "
              onClick={(e) => {
                e.preventDefault();
                setIsLoggingIn(!isLoggingIn);
              }}
            >
              {isLoggingIn ? "Non hai un account?" : "Hai già un account?"}
            </a>
          </div>
        </div>

        <div className="flex flex-col">
          <Input
            placeholder={"Password"}
            type={"password"}
            required
            {...password("password")}
          />
        </div>

        {isRunningMutation && <Alert variant={Variant.INFO}>Caricamento</Alert>}
        {operationFailed && mutationResultTypename && (
          <Alert variant={Variant.ERROR}>
            {getMessageForError(mutationResultTypename)}
          </Alert>
        )}

        <div className="flex justify-center flex-grow space-x-3 my-7">
          <Button text={isLoggingIn ? "Accedi" : "Registrati"} />
        </div>
      </form>
    </Modal>
  );
};