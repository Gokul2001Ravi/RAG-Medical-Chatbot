# from langchain_huggingface import HuggingFaceEmbeddings

# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException

# logger = get_logger(__name__)

# def get_embedding_model():
#     try:
#         logger.info('Initializing our huggingface embedding model')

#         model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#         logger.info('HuggingFace Embedding model loaded sucessfully..')

#         return model
    
#     except Exception as e:
#         error_message = CustomException("Error Occured while loading embedding model", e)
#         logger.error(str(error_message))
#         raise error_message
    
# from langchain_huggingface import HuggingFaceEmbeddings
# from app.common.logger import get_logger
# from app.common.custom_exception import CustomException
# import os

# logger = get_logger(__name__)

# def get_embedding_model():
#     try:
#         logger.info('Initializing our huggingface embedding model')

#         huggingface_token = os.environ.get("HF_TOKEN")

#         if not huggingface_token:
#             raise CustomException("Hugging Face token not found in environment variables")

#         model = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2",
#             huggingfacehub_api_token=huggingface_token
#         )

#         logger.info('HuggingFace Embedding model loaded successfully..')

#         return model
    
#     except Exception as e:
#         error_message = CustomException("Error Occurred while loading embedding model", e)
#         logger.error(str(error_message))
#         raise error_message
    
from langchain_huggingface import HuggingFaceEmbeddings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from dotenv import load_dotenv

logger = get_logger(__name__)
load_dotenv()  # Load .env vars

def get_embedding_model():
    try:
        logger.info('Initializing our huggingface embedding model')

        # DO NOT manually fetch or pass the token
        model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        logger.info('HuggingFace Embedding model loaded successfully..')

        return model

    except Exception as e:
        error_message = CustomException("Error Occurred while loading embedding model", e)
        logger.error(str(error_message))
        raise error_message


