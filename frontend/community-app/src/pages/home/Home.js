import Navbar from "../../components/navbar/Navbar";
import axios from 'axios';
import {useEffect, useState} from 'react'


export default function Home() {

    const [questions, setQuestions] = useState([])

    useEffect(() => {
        axios
            .get(`http://127.0.0.1:5000/question`)
            .then(res => {
                console.log(res)
                setQuestions(res.data)
             })
    }, [])

    return (
        <>
        {questions.map(ques => {
            return(
                <>
                <h1>Questions</h1>
                <h3>{ques.created}</h3>
                <h3>{ques.id}</h3>
                <h3>{ques.likes}</h3>
                <h3>{ques.title}</h3>
                <h3>{ques.value}</h3>
                </>
            )
        })}
        </>
    )
}