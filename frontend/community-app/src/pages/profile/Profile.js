import { useParams } from "react-router-dom"

export default function Profile() {
    const {userID} = useParams();
    return (
        <>
            This is Profile {userID}
            <h1>{userID}</h1>
        </>
    )
}