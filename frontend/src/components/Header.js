import React from 'react'
import './Header.css'
// import DockerLogo from '../images/docker-logo.png'
import NewLogo from '../images/newlogo.png'

function Header() {
    return (
        <div className='Header'>
            <img src={NewLogo} alt="docker logo" className='Header__logo'/>
            <div className='Header__heading'>
                <h3 className='Header__headingtext'>Docker Management Console</h3>
            </div>
        </div>
    )
}

export default Header
