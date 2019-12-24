/** @jsx jsx */
import "react-day-picker/lib/style.css";

import DayPickerInput from "react-day-picker/types/DayPickerInput";
import { jsx } from "theme-ui";

type DatePickerProps = {
  value: Date;
  onValueChange?: (day: Date) => void;
};

export const DatePicker: React.SFC<DatePickerProps> = ({
  value,
  onValueChange,
}) => {
  const parseDate = (str: string, format: string, locale: string) => {
    const timestamp = Date.parse(str);

    if (!isNaN(timestamp)) {
      const date = new Date(timestamp);
      return date;
    }
    return undefined;
  };

  const formatDate = (date: Date, format: string, locale: string) =>
    date.toISOString().split("T")[0];

  return (
    <DayPickerInput
      formatDate={formatDate}
      parseDate={parseDate}
      format="yyyy-MM-dd"
      value={value}
      onDayChange={onValueChange}
    />
  );
};
