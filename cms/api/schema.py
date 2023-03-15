from page.models import GenericPage as GenericPageModel
import strawberry
from api.types import GenericPage
from wagtail.models import Site


@strawberry.type
class SiteNotFoundError:
    message: str


@strawberry.type
class Query:
    @strawberry.field
    def page(
        self,
        code: str,
        slug: str,
        language: str,
    ) -> GenericPage | SiteNotFoundError | None:

        if not (site := Site.objects.filter(hostname=code).first()):
            return SiteNotFoundError(message=f"Site `{code}` not found")

        page = (
            GenericPageModel.objects.in_site(site)
            .filter(locale__language_code=language, slug=slug)
            .first()
        )

        if not page:
            return None

        return GenericPage.from_model(page)

    @strawberry.field
    def pages(self, code: str, language: str) -> list[GenericPage]:
        if not (site := Site.objects.filter(hostname=code).first()):
            return []

        return [
            GenericPage.from_model(page)
            for page in GenericPageModel.objects.in_site(site).filter(
                locale__language_code=language
            )
        ]


schema = strawberry.Schema(query=Query)