const axios = require('axios');
const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000/'
})

const question = {
    state: {
        questions: [],
        qid: null,
        value: null,
        question_cid: null,
        question_uid: null,
        created: null
    },

    mutations: {
        setQuestions(state, payload) {
            state.questions = payload
            console.log('Questions:', state.questions)
        },

        setNewViewQuestion(state, qid) {
            let qObj;
            for (let i in state.questions) {
                if (state.questions[i].id == qid) qObj = state.questions[i];
            }
            state.qid = qObj.id
            state.value = qObj.value
            state.question_cid = qObj.cid
            state.question_uid = qObj.uid
            console.log('Current question : ', state.value)
        }
    },

    actions: {
        async GetQuestions(context) {
            let res = await axiosInstance.get('question')
            if (res.status === 200) {
                context.commit('setQuestions', res.data)
                console.log('Question Reponse: ', res.data)
            } else {
                console.log(res.data)
                context.dispatch('ShowError', res.data)
            }
        },

        async CreateQuestion(context, formData) {
            console.log(formData)
            let res = await axiosInstance.post(
                formData.cid + '/question',
                {
                    "title": formData.title,
                    "value": formData.value,
                    "uid": formData.uid,
                    "cid": formData.cid
                }
            )
            if (res.status === 200) {
                console.log(res.data);
                context.dispatch('GetQuestions')
                context.dispatch('ShowError', 'Your question has been registered')
            } else {
                console.log(res.data)
                context.dispatch('ShowError', 'Please log in / sign up')
            }
        },
    }
}

export default question