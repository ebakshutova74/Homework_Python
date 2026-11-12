import uuid
from yougile_api import YougileProjectsApi

BASE_URL = "https://yougile.com"
TOKEN = "ВСТАВЬТЕ_ВАШ_ТОКЕН_СЮДА"

api = YougileProjectsApi(base_url=BASE_URL, token=TOKEN)


# --- ПОЗИТИВНЫЕ ТЕСТЫ ---

def test_create_project_positive():
    title = f"AutoTest Create {uuid.uuid4().hex[:6]}"
    response = api.create_project({"title": title})

    assert response.status_code == 201
    body = response.json()
    assert "id" in body

    api.update_project(body["id"], {"deleted": True, "title": title})


def test_get_project_positive():
    title = f"AutoTest Get {uuid.uuid4().hex[:6]}"
    create_res = api.create_project({"title": title})
    project_id = create_res.json()["id"]

    response = api.get_project(project_id)
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == project_id
    assert body["title"] == title

    api.update_project(project_id, {"deleted": True, "title": title})


def test_update_project_positive():
    old_title = f"AutoTest Old {uuid.uuid4().hex[:6]}"
    create_res = api.create_project({"title": old_title})
    project_id = create_res.json()["id"]

    new_title = f"AutoTest New {uuid.uuid4().hex[:6]}"
    response = api.update_project(project_id, {"title": new_title})
    assert response.status_code == 200
    assert response.json()["id"] == project_id

    get_res = api.get_project(project_id)
    assert get_res.json()["title"] == new_title

    api.update_project(project_id, {"deleted": True, "title": new_title})


# --- НЕГАТИВНЫЕ ТЕСТЫ ---

def test_create_project_empty_title_negative():
    response = api.create_project({"title": ""})
    assert response.status_code == 400


def test_get_project_nonexistent_id_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(fake_id)
    assert response.status_code == 404


def test_update_project_invalid_payload_negative():
    title = f"AutoTest NegUpdate {uuid.uuid4().hex[:6]}"
    create_res = api.create_project({"title": title})
    project_id = create_res.json()["id"]

    response = api.update_project(project_id, {"title": 12345})
    assert response.status_code == 400

    api.update_project(project_id, {"deleted": True, "title": title})
