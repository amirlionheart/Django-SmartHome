# Smart Home API (Django REST Framework)

REST API для управления датчиками и измерениями температуры.

---

## 🚀 Возможности

- Создание и редактирование датчиков
- Добавление температурных измерений
- Получение списка датчиков
- Получение детальной информации с историей измерений

---

## 🧱 Технологии

- Python
- Django
- Django REST Framework
- PostgreSQL

---

## 📦 Модели

**Sensor**
- name — название
- description — описание (опционально)

**Measurement**
- sensor — датчик (FK)
- temperature — температура
- created_at — время измерения

---

## ⚙️ Установка

```bash
git clone <repo_url>
cd smart_home
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
cd smart_home

