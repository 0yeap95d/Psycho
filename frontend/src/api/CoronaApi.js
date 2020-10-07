import Axios from "axios"

const apiUrl = "https://j3d203.p.ssafy.io/api"

const requestCorona = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "covid19data/Covid19Info", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}

const CoronaApi = {
  requestCorona: (data, callback, errorCallback) => requestCorona(data, callback, errorCallback),
}

export default CoronaApi
