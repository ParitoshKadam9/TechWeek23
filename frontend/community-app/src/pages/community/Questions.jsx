import { useParams } from "react-router-dom"

export default function Questions() {
    const {communityID} = useParams();
    return(
        <>
        <h1>Questions</h1>
        </>
    )
}