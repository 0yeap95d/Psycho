import Axios from "axios";

const apiUrl = "http://j3d2203.p.ssafy.io:8000/stores";

const requestStore = (callback, errorCallback) => {
    Axios.get(apiUrl + '/restaurants')
        .then(res => callback(res))
        .catch(error => errorCallback(error))
}

const requestRecStore = (data, callback, errorCallback) => {
    Axios.post(apiUrl + '/recommend/stores', data)
        .then(res => callback(res))
        .catch(error => errorCallback(error)) 
}

const StoreApi = {
    requestStore: (callback, errorCallback) => requestStore(callback, errorCallback),
    requestRecStore: (data, callback, errorCallback) => requestRecStore(data, callback, errorCallback),
}

export default StoreApi