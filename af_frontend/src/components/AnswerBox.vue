<template>
    <div class="box">
        <div class="user">{{ username }}</div>
        <div class="content">
            <div class="left">
                + : {{ likes }}
            </div>
            <div class="right">
                {{ answer }}
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "AnswerBox",
    props: {
        username: String,
        likes: Number,
        answer: String
    },
}
</script>
<style scoped>
    .box{
        min-height:15vh ;
        display: flex;
        flex-direction: column;
        border: 1px solid rgb(176, 176, 31);
        border-radius: 5px;
        padding: 20px;
        margin-top: 2vh;
        margin-bottom: 2vh;
    }
    .user{
        font-size: 2vh;
        color: rgb(176, 176, 31);
    }
    .content{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        margin-top: 2vh;
    }
    .left{
        width: 10%;
                color: rgb(176, 176, 31);

    }
    .right{
        font-size: 3vh;
        color: white;
    }
</style>