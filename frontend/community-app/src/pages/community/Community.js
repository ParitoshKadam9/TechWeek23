import { useParams, useSearchParams } from "react-router-dom"

export default function Community() {
    const {communityID} = useParams();
    return (
        <>
            This is community {communityID}
            <h1>{communityID}</h1>
        </>
    )
}