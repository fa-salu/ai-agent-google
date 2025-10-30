from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def get_current_time(city: str) -> dict:
    """Returns the current local time in the given city."""
    try:
        geolocator = Nominatim(user_agent="time_agent")
        location = geolocator.geocode(city)
        if not location:
            return {"status": "error", "message": f"City '{city}' not found."}

        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
        if not timezone_str:
            return {"status": "error", "message": f"Timezone not found for {city}."}

        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "success",
            "city": city,
            "timezone": timezone_str,
            "time": local_time,
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
