import Axios from "axios"

const apiUrl = "http://localhost:8000/covid19data"

const requestCorona = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "/Covid19Info", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}

const CoronaApi = {
  requestCorona: (data, callback, errorCallback) => requestCorona(data, callback, errorCallback),
}

export default CoronaApi
