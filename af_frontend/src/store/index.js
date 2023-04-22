import { createStore } from "vuex";

import user from '@/store/user'
import community from '@/store/community'
import question from '@/store/question'
import answer from '@/store/answer'

export default createStore({
    state: {
        error: "",
        isLoggedIn: false,
    },
    getters: {

    },
    mutations: {
        setError(state, payload) {
            state.error = payload
            console.log('Error Set')
        },
        clearError(state) {
            state.error = "";
            console.log('Error Cleared')
        },
        setLogIn(state) {
            state.isLoggedIn = true;
        }
    },
    actions: {
        ShowError(context, error) {
            context.commit('setError', error)
            setTimeout(() => { context.commit('clearError') }, 3000)
        }
    },
    modules: {
        user: user,
        community: community,
        question: question,
        answer: answer
    }
});
