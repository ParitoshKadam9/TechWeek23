<template>
    <div class="head">
        <div class="left">
            <div class="askedBy"><div class="ask">Asked By </div>: <div class="name"> {{ userName }}</div></div>
            <div class="question">
                {{ question }}
            </div>
        </div>
            <div class="right">
                <div class="questionID">#{{ questionID }}</div>
                <div class="date">{{ date }}</div>
            </div>
    </div>
    <div class="Answers">
        <div class="ansHead">
            <div class="leftans">Answers :</div>
            <div class="rightans">+ Answer</div>
        </div>
        <AddAnswer/>
        <div class="ansList">
            <AnswerBox/>
            <AnswerBox/>
            <AnswerBox/>
            <AnswerBox/>
        </div>
    </div>
</template>
<script>
import AddAnswer from '@/components/AddAnswer.vue';
import AnswerBox from '../components/AnswerBox.vue';

export default{
    name: "QuestionView",
    data() {
        return {
            question: "If I have 3 apples and I give 2 to my friend ho much do i have. If I have 3 apples and I give 2 to my friend ho much do i have. If I have 3 apples and I give 2 to my friend ho much do i have",
            questionID: "7662",
            date: "26/11/08",
            userName: "Paritosh Kadam"
        };
    },
    components: { AnswerBox, AddAnswer }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.rightans{
    width: fit-content;
    height: fit-content;
    padding: 1vh;
    background: rgb(176, 176, 31);
    border-radius:5px ;
}

.Answers{
    display: flex;
    flex-direction: column;
justify-content: center;
    margin-left: auto;
    margin-right: auto;
    width: 130vh;
    margin-top: 5vh;
}
.ansHead{
    font-size: 3vh;
    color: white;
    margin-bottom: 3vh;
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: space-between;
    width: 130vh;
}

.head{
    width: 130vh;
    margin-top: 10vh;
    margin-left: auto;
    margin-right: auto;
    color: white;
    height: 20vh;
    display: flex;
    flex-direction: row;
    align-items: end;
    justify-content: space-between;
    border-bottom: 2px solid rgb(176, 176, 31);
    padding-bottom: 3vh;
}
.ask{
    border-bottom: 1px solid white;
    margin-right: 5px;
}
.askedBy{
    display: flex;
    flex-direction: row;
    align-items: center;
}
.name{
    margin-left: 5px;
    color: rgb(176, 176, 31);
}
.question{
    font-size: 4vh;
    width: 80%;
    margin-top: 5vh;
}
.right{
    display: flex;
    flex-direction: column;
    align-items: end;
        font-family: 'Montserrat', sans-serif;
    height: 10vh;
    color: gray;
    justify-content: space-around;
}
</style>