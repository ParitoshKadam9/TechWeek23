const axios = require('axios')
const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000'
})
const answer = {
    state: {
        answers: [],
    },

    mutations: {
        setAnswers(state, payload) {
            state.answers = payload
            console.log('Answers:', state.answers)
        }
    },

    actions: {
        async GetAnswers(context) {
            let res = await axiosInstance.get('/answer')
            if (res.status === 200) {
                context.commit('setAnswers', res.data)
            } else {
                console.log(res.data)
                context.dispatch('ShowError', res.data)
            }
        },

        async CreateAnswer(context, formData) {
            console.log(formData)
            let res = await axiosInstance.post(
                formData.qid + '/answer',
                {
                    'value': formData.value,
                    'uid': formData.uid,
                    'qid': formData.qid
                }
            )
            if (res.status === 200) {
                console.log(res.data)
                context.dispatch('GetAnswers')
                context.dispatch('ShowError', 'Your answer has been added')
            } else {
                console.log(res.data)
                context.dispatch('ShowError', 'Please log in')
            }
        }
    }
}

export default answer 