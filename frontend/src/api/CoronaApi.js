import Axios from "axios"

// const apiUrl = "http://localhost:8000/covid19data"
const apiUrl = "https://j3d203.p.ssafy.io:8000/covid19data"

const requestCorona = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "/Covid19Info", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}
const requestCoronaGenAge = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "/Covid19GenAgeInfo", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}
const requestCoronaSido = (data, callback, errorCallback) => {
  Axios.post(apiUrl + "/Covid19SidoInfo", data)
    .then((res) => callback(res))
    .catch((error) => errorCallback(error))
}

const CoronaApi = {
  requestCorona: (data, callback, errorCallback) => requestCorona(data, callback, errorCallback),
  requestCoronaGenAge: (data, callback, errorCallback) => requestCoronaGenAge(data, callback, errorCallback),
  requestCoronaSido: (data, callback, errorCallback) => requestCoronaSido(data, callback, errorCallback),
}

export default CoronaApi
