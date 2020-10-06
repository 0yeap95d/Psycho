import Axios from "axios";

const apiUrl = "http://localhost:8000/stores";

const requestStore = (callback, errorCallback) => {
    Axios.get(apiUrl + '/restaurants')
        .then(res => callback(res))
        .catch(error => errorCallback(error))
}

const requestRecStore = (callback, errorCallback) => {

    Axios.post(apiUrl + '/recommend/stores',
    {
        pos_x: 126.97,
        pos_y: 37.57,
        gender: "1.남성",
        age: "4.40대",
        address: "서울특별시 종로구 도렴동 60번지"
    })
        .then(res => callback(res))
        .catch(error => errorCallback(error)) 
}

const StoreApi = {
    requestStore: (callback, errorCallback) => requestStore(callback, errorCallback),
    requestRecStore: (callback, errorCallback) => requestRecStore(callback, errorCallback),
}

export default StoreApi