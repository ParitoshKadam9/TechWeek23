<template>
    <div class="CommBox">
        <div class="left">
            <div class="quest">
                <div class="CommName">
                    <div class="question">{{ question }}</div>
                </div>
                <div class="dot">...</div>
            </div>
        </div>
        <div class="right">

            <div class="QuestionID">
                #{{ questionID }}
            </div>
            <div class="date">
                {{ date }}
            </div>
            <div class="likes">
                LikeIcon : {{ likes }} likes
            </div>
        </div>
    </div>
</template>
<script>
export default {

    name: "QuestionBox",
    data() {
        return {
            question : "If I have 3 apples and I give 2 to my friend ho much do i have",
            date: "27/02/23",
            likes:"99",
            questionID: "4199"
        }
    }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.quest{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
.CommBox {
    width: 130vh;
    margin-top: 2vh;
    height: 11vh;
    /* margin-left: auto;
    margin-right: auto; */
    background: #1e1e1e;
    border-radius: 5px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 5vh;
    cursor: pointer;
    color: rgb(176, 176, 31);
    transition: 0.1s;
}
.dot{
    font-size: 5vh;
    margin-left: 1vh;
}


.CommName {
    font-size: 5vh;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    width: 100vh;
    height:7vh;
    display: flex;
    flex-wrap: wrap;
    overflow-x: hidden;
    overflow-y: hidden;
}
.right{
    color: gray;
    font-family: 'Montserrat', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    height: 15vh;
}

.CommID {
    font-size: 3vh;
    font-family: 'Montserrat', sans-serif;
    color: gray;
    margin-right: 5vh;

}</style>