import http from '../custom_axios'


    const getAll = () => {
        return http.get('/tests')
    }
    function getOne(id) {
        // will need to go into django/urls and add this path
        return http.get(`/tests/{id}`)
    }
    const createTest = (data, user) => {
        return http.post(`/test`, {data, user})
    }

    export{createTest, getAll, getOne}

// export default function TestDataService () {
//     function getAll() {
//         return http.get('/tests')
//     }
//     function getOne(id) {
//         // will need to go into django/urls and add this path
//         return http.get(`/tests/{id}`)
//     }
//     function createTest(data) {
//         return http.post(`/test/{id}`, data)
//     }
// }