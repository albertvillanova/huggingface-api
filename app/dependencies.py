from fastapi.security import HTTPBearer


# credentials.scheme "Bearer", credentials.credentials = "MY-TOKEN"
security = HTTPBearer(auto_error=False)  # `auto_error=False` allows credentials = None
