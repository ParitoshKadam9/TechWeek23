import CommunityCard from "./CommunityCard"
import "../../styles/Communities.css"
import Navbar from "../../components/navbar/Navbar"

const communityData = [
    {
        comNumber : 1,
        comName : 'Community 1',
        comImage : "https://images.unsplash.com/photo-1677257355254-f139273ac6e1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=800&q=60https://images.unsplash.com/photo-1677257355254-f139273ac6e1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=800&q=60",
        comDesc : "This is Community 1"
    },
    {
        comNumber : 2,
        comName : 'Community 2',
        comImage : "https://images.unsplash.com/photo-1677269309550-53d5e989f890?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw4fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=800&q=60",
        comDesc : "This is Community 2"
    },
]

export default function Communities() {
    return (
        <>
        <Navbar />
        <h1 style={{textAlign:'center'}}>Communities</h1>
        <div className="communities-div">
        {
            communityData.map((community) => {
                return(
                    <CommunityCard 
                        id = {community.comNumber}
                        name={community.comName}
                        description = {community.comDesc}
                        key = {community.comNumber}
                        image = {community.comImage}
                    />
                )
            })
        }
        </div>
        </>
    )
}