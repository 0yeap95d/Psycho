import Axios from "axios";

const apiUrl = "http://localhost:8000/stores";

const requestHotel = (callback, errorCallback) => {
    Axios.get(apiUrl + '/hotels' + '?name=종로',)
        .then(res => callback(res))
        .catch(error => errorCallback(error))
}

const HotelApi = {
    requestHotel: (callback, errorCallback) => requestHotel(callback, errorCallback),
}

export default HotelApi