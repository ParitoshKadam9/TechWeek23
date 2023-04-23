const axios = require('axios')
const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000/category'
})
const community = {
    state: {
        communities: [],
        cid: null,
        title: null,
        description: null,
        created: null,
        community_uid: null,
    },
    getters: {
        getCommunities: (state, getters) => (id) => {
            let owner = getters.getUserById(id)
            const commObj = {
                cid: state.cid,
                title: state.title,
                description: state.description,
                created: state.created,
                owner_uobj: owner
            }
            return commObj
        }
    },

    mutations: {
        setCommunities(state, payload) {
            state.communities = payload
            console.log('Comms:', state.communities)
        },
        setNewViewCommunity(state, cid) {
            let commObj;
            for (let i in state.communities) {
                if (state.communities[i].id === cid) commObj = state.communities[i];
            }
            state.cid = commObj.id
            state.title = commObj.title
            state.description = commObj.description
            state.created = commObj.created
            state.community_uid = commObj.uid
            console.log('Current comm:', state.title)
        }
    },

    actions: {
        async GetCommunities(context) {
            let res = await axiosInstance.get('')
            if (res.status === 200) {
                context.commit('setCommunities', res.data)
                console.log('Response:', res.data)
            } else {
                console.log(res.data)
                context.dispatch('ShowError', res.data)
            }
        },

        async CreateCommunity(context, formData) {
            let res = await axiosInstance.post('', {
                'uid': formData.uid,
                'title': formData.title,
                'description': formData.description
            })

            if (res.status === 200) {
                console.log(res.data)
                context.dispatch('GetCommunities')
                context.dispatch('ShowError', 'Your community has been created')
            } else {
                console.log(res.data)
                context.dispatch('ShowError', 'Please log in first');
            }
        },

        async DeleteCommunity(context) {
            let res = await axiosInstance.delete('/' + context.state.cid)
            if (res.status === 200) {
                context.dispatch('ShowError', 'You have deleted this community')
            } else {
                context.dispatch('ShowError', 'Please log in first')
            }
        }
    }
}

export default community 