<template>
    <div class="box">
        <div class="QuestionID">
            #{{ questionID }}
        </div>
        <div class="answer">
            <texarea placeholder="Type Answer here"/>
        </div>
    </div>
</template>
<script>
export default {
    name: "AddAnswer",
    data() {
        return {
            questionID: '8988'
        }
    }
}
</script>
<style>
</style>