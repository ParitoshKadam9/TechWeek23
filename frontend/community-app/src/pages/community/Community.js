import { Button } from "@mui/material";
import { useParams } from "react-router-dom"

export default function Community() {
    const {communityID} = useParams();
    return (
        <>
            This is community {communityID}
            <h1>{communityID}</h1>
            <Button variant="contained" href={`./${communityID}/questions`}>
                Ask Questions
            </Button>
        </>
    )
}