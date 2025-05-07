E-commerce-Platform-Backend/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py
│   │       │   ├── users.py
│   │       │   ├── products.py
│   │       │   ├── cart.py
│   │       │   ├── orders.py
│   │       │   ├── reviews.py
│   │       │   ├── admin.py
│   │       │   ├── notifications.py
│   │       │   └── uploads.py
│   │       └── __init__.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   └── __init__.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── product.py
│   │   │   ├── cart.py
│   │   │   ├── order.py
│   │   │   ├── review.py
│   │   │   ├── review_vote.py
│   │   │   ├── notification.py
│   │   │   └── __init__.py
│   │   ├── repositories/
│   │   │   ├── user_repo.py
│   │   │   ├── product_repo.py
│   │   │   ├── cart_repo.py
│   │   │   ├── order_repo.py
│   │   │   └── review_repo.py
│   │   └── __init__.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── review.py
│   │   ├── auth.py
│   │   ├── notification.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   ├── cart_service.py
│   │   ├── order_service.py
│   │   ├── review_service.py
│   │   ├── auth_service.py
│   │   └── notification_service.py
│   │
│   ├── static/
│   │   └── uploads/
│   │
│   ├── main.py
│   └── __init__.py
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── frontend/                  # React-based admin & customer UI
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/
│   │   ├── App.tsx
│   │   └── main.tsx
│   └── package.json
│
├── alembic.ini
