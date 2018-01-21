from pytest import raises
from taskit.application.repositories.errors import EntityNotFoundError


def test_entity_not_found_error() -> None:
    with raises(EntityNotFoundError):
        raise EntityNotFoundError("Entity not found in repository!")
