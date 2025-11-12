import pytest
from main import Tasklist


@pytest.fixture
def sample_basic_tasks() -> list[list]:
    basic_tasks = [
        ["get plane sharpening jig", "tune plane blade", "finish pt holder"],
        ["make flat sharpening plates", "flatten planes", "finish pt holder"],
        ["make flat sharpening plates", "tune plane blade"],
        ["dry backpack rack", "place hardware on backpack rack", "hang backpack rack"],
        ["clean garage", "get parking system figured"],
    ]
    return basic_tasks


def test_basic_functionality(sample_basic_tasks: list[list[str]]) -> None:
    house_tasks = Tasklist()
    for task_run in sample_basic_tasks:
        house_tasks.add_task_run(task_run)

    assert house_tasks.get_available_tasks() == [
        "get plane sharpening jig",
        "make flat sharpening plates",
        "dry backpack rack",
        "clean garage",
    ]
