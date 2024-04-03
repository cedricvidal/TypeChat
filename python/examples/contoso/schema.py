from typing_extensions import Literal, TypedDict, Annotated, Doc


class UnknownText(TypedDict):
    """
    Use this type for order items that match nothing else
    """

    type: Literal["Unknown"]
    text: Annotated[str, Doc("The text that wasn't understood")]


class ProductFilter(TypedDict):
    type: Literal["Tent", "Pole", "Sleeping bag", "Hiking shoes"]


class Query(TypedDict):
    type: Literal["Query"]
    items: list[ProductFilter | UnknownText]
