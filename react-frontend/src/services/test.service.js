import http from '../custom_axios'

export default function TestDataService () {
    function getAll() {
        return http.get('/tests')
    }
    function getOne(id) {
        // will need to go into django/urls and add this path
        return http.get(`/tests/{id}`)
    }
    function createTest(data) {
        return http.post(`/test/{id}`, data)
    }
}