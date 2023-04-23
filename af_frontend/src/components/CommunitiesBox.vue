<template>
    <div class="CommBox">
        <div class="left">
                <div class="CommName">{{ title }}</div>
            </div>
            <div class="right">
                <div class="CommID">#{{ description }}</div>
        </div>
    </div>
</template>
<script>
export default {
    name: "CommuntiesBox",
    data() {
        return {
            title: "CS F407",
            description: "4199"
            }
        }
    }
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

    .CommBox{
        width: 100vh;
        margin-top: 2vh;
        min-height: 15vh;
        margin-left: auto;
        margin-right: auto;
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
    .CommBox:hover{
        background: rgb(176, 176, 31);
        color: black;
    }
    .CommName{
        font-size: 5vh;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  
    }
    .CommID{
        font-size: 3vh;
       font-family: 'Montserrat', sans-serif;  color: gray;
        margin-right: 5vh;
        
    }
</style>