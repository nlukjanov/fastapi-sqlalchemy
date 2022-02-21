from base64 import encode
from datetime import datetime, timedelta
from pathlib import Path

import jwt
from cryptography.hazmat.primitives import serialization

# user1 = eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29mZmVlbWVzaC5pbyIsInN1YiI6IjIyYWI4YTZkLTA0YmMtNDM1Ni1iYzU0LTc4ZmU1NTdmZDUwMyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjEvdG9kbyIsImlhdCI6MTY1NjM2NDUwMi41Mzg3NjksImV4cCI6MTY1NjQ1MDkwMi41Mzg3Njl9.nwEQ8jKyzwDi3TqiRTqh2uSnXZxVUZl890iEZNrVkcRYMdZpb_sPVYZ2Q3C0eW_jUaH9io44SCfdBJsxZgdNHkECrvqCa-RaONQiHWuxK5YQgBSS0KnSFHVBsxAzPMNRnOTNZxuRwn7ffP7jG7WislvJTZP7PEPOi3DRIlP2Cg3tpk-xVBX1buXptOLqZwkjxpdOjlrC3vSZ2z_kLoGbU8aB152-aGAzRhmmh6_2gpO0JgHQ-gQ2py86ga7ev0XhmK_F6vW9S9cJyTZx9J9tvUWQt0aLPjLQlXfOtWK-E6YVE34-bnU9R34LJAVlqVZ6NPgP_sJ0O9OrUDQqFPVRLA

# user2 = eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29mZmVlbWVzaC5pbyIsInN1YiI6IjdmMzg1ODI2LTIwZGEtNDRlZS04ZTI2LWMxYzkwNGIwOTU2MyIsImF1ZCI6Imh0dHA6Ly8xMjcuMC4wLjEvdG9kbyIsImlhdCI6MTY1NjM3OTczNC41MTE5OTgsImV4cCI6MTY1NjQ2NjEzNC41MTE5OTh9.UVytv9gVbcs6dQJ2fv-aIYpPnozS4glgpcT097uJdptxB1hU5nGTwzXxrGrHJh3TMi4yDfAt7AqwuzW6s8YburYyXKNHsaPnXxwtrqibeKp4GDBL2BLmaFiFPYak6PCBTUIR8TuqsiFPS0dBMXNnZkkWdqLVukpYOGmi98-iIwick3HsbiczfpjEBu0GMeBOe6BO9o0dxXzZtxT8y1LoDZY4OMPANFcBvVXLLgDeIE8-DLFKvQLcB2cIFS_gBr9xdOA-mm1YtHEgfabaa3emMgVQSWgcj9KGS2rDe_Qvc3azcL2JtYYe4QhislKKY5LGn3YlKJeN69vKwpjMSJllZw


def generate_jwt():
    now = datetime.utcnow()
    payload = {
        'iss': 'https://auth.coffeemesh.io',
        'sub': '7f385826-20da-44ee-8e26-c1c904b09563',
        'aud': 'http://127.0.0.1/todo',
        'iat': now.timestamp(),
        'exp': (now + timedelta(hours=24)).timestamp(),
    }

    private_key_text = Path('private_key.pem').read_text()
    private_key = serialization.load_pem_private_key(
        private_key_text.encode(),
        password=None
    )

    return jwt.encode(payload=payload, key=private_key, algorithm='RS256')


print(generate_jwt())
