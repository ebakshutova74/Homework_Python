import pytest
from sqlalchemy import create_engine, text

DB_CONNECTION_STRING = "postgresql://myuser:mypassword@localhost:5432/mydatabase"


@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(DB_CONNECTION_STRING)
    yield engine
    engine.dispose()


def test_add_subject(db_engine):
    test_id = 99991
    test_title = "Автотестирование на Python"

    with db_engine.begin() as conn:
        # Очистка перед тестом для гарантии стабильности при повторном запуске
        conn.execute(text("DELETE FROM subjects WHERE subject_id = :id"), {"id": test_id})

        # 1. Добавление записи
        conn.execute(
            text("INSERT INTO subjects (subject_id, subject_title) VALUES (:id, :title)"),
            {"id": test_id, "title": test_title}
        )

        # 2. Проверка, что запись добавлена
        row = conn.execute(
            text("SELECT subject_title FROM subjects WHERE subject_id = :id"),
            {"id": test_id}
        ).fetchone()

        assert row is not None
        assert row[0] == test_title

        # 3. Удаление созданных данных за собой
        conn.execute(text("DELETE FROM subjects WHERE subject_id = :id"), {"id": test_id})


def test_update_subject(db_engine):
    test_id = 99992
    initial_title = "Начальное название предмета"
    updated_title = "Обновленное название предмета"

    with db_engine.begin() as conn:
        # Очистка перед тестом
        conn.execute(text("DELETE FROM subjects WHERE subject_id = :id"), {"id": test_id})

        # Подготовка данных: создаем запись для изменения
        conn.execute(
            text("INSERT INTO subjects (subject_id, subject_title) VALUES (:id, :title)"),
            {"id": test_id, "title": initial_title}
        )

        # 1. Изменение записи
        conn.execute(
            text("UPDATE subjects SET subject_title = :title WHERE subject_id = :id"),
            {"title": updated_title, "id": test_id}
        )

        # 2. Проверка, что запись изменилась
        row = conn.execute(
            text("SELECT subject_title FROM subjects WHERE subject_id = :id"),
            {"id": test_id}
        ).fetchone()

        assert row is not None
        assert row[0] == updated_title

        # 3. Удаление созданных данных за собой
        conn.execute(text("DELETE FROM subjects WHERE subject_id = :id"), {"id": test_id})


def test_delete_subject(db_engine):
    test_id = 99993
    test_title = "Предмет для удаления"

    with db_engine.begin() as conn:
        # Очистка перед тестом
        conn.execute(text("DELETE FROM subjects WHERE subject_id = :id"), {"id": test_id})

        # Подготовка данных: создаем запись для удаления
        conn.execute(
            text("INSERT INTO subjects (subject_id, subject_title) VALUES (:id, :title)"),
            {"id": test_id, "title": test_title}
        )

        # 1. Удаление записи
        conn.execute(text("DELETE FROM subjects WHERE subject_id = :id"), {"id": test_id})

        # 2. Проверка, что запись удалена
        row = conn.execute(
            text("SELECT subject_title FROM subjects WHERE subject_id = :id"),
            {"id": test_id}
        ).fetchone()

        assert row is None