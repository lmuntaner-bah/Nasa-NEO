from pydantic import BaseModel, ValidationError
from typing import Type, Optional
import pandas as pd

class NeoJobParams(BaseModel):
    alias_name: str = 'official_name'
    alias_limited_name: str = 'short_name'
    alias_first_date: str = 'first_date_detected'
    alias_last_date: str = 'last_date_detected'
    bucket_name: str = 'neo-pipeline'
    file_name: str = 'neo_interm_data.csv'
    haz_asteroid: str = 'true'
    local_dir: str = "../data/temp_processed"

class NeoDF(BaseModel):
    id: int
    official_name: Optional[str]
    short_name: Optional[str]
    absolute_magnitude_h: float
    is_potentially_hazardous_asteroid: bool
    is_sentry_object: bool
    kilometers_estimated_diameter_min: float
    kilometers_estimated_diameter_max: float
    perihelion_distance: float
    aphelion_distance: float
    first_date_detected: Optional[str]
    last_date_detected: Optional[str]
    orbit_class_description: Optional[str]

class DataFrameValidationError(Exception):
    """Custom exception for DataFrame validation errors."""

def validate_dataframe(df: pd.DataFrame, model: Type[BaseModel]):
    """
    Validates each row of a DataFrame against a Pydantic model.
    Prints errors if any row fails validation and returns a boolean indicating the validation result.
    
    Parameters:
    - df: DataFrame to validate.
    - model: Pydantic model to validate against.
    
    Returns:
    - bool: True if all rows pass validation, False otherwise.
    """
    errors = []
    
    for i, row in enumerate(df.to_dict(orient="records")):
        try:
            model(**row)
        except ValidationError as e:
            error_message = f"Row {i} failed validation: {e}"
            print(error_message)
            errors.append(error_message)
    
    if errors:
        return False
    return True