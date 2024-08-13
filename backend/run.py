import os
from app import create_app


config_name = os.environ["CONFIG_MODE"]
app = create_app(config_name)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT") or 5000)
