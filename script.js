
const education = [
    {degree: "Associate of Science", school: "Weber State University", year: "2019",  logo: "./images/weber-state-logo.jpg", link: "https://www.weber.edu/"},
    {degree: "Bachelor of Elementary Education", school: "Utah State University", year: "2025", logo: "./images/utah-state-logo1.jpg", link: "https://www.usu.edu/" },
    {degree: "Master of Education", school: "Purdue University", year: "2026", logo: "./images/purdue-logo.jpg", link: "https://www.purdue.edu/"}    
];

const jobs = [
    {logo: "./images/chris.png", title: "Chrysalis", year: "2022-Present", description: ""},
    {logo: "./images/school.jfif", title: "Title 1 Tutor", year: "2018-2019", description: ""},
    {logo: "./images/hillfield.jfif", title: "HillField Dental Assistant", year: "2016-2018", description: ""}
];

const tech = [
    {logo: "./images/react-logo.jpg", title: "React.js", link: "https://github.com/Bosser16"},
    {logo: "./images/css-logo.png", title: "CSS", link: "https://github.com/Bosser16"},
    {logo: "./images/html-logo.jpg", title: "HTML", link: "https://github.com/Bosser16"},
    {logo: "./images/javascript-logo.jpg", title: "JavaScript", link: "https://github.com/Bosser16"},
    {logo: "./images/java-logo.png", title: "Java", link: "https://github.com/Bosser16"},
    {logo: "./images/python-logo.jpg", title: "Python", link: "https://github.com/Bosser16"},
    {logo: "./images/c-logo.png", title: "C", link: "https://github.com/Bosser16"},
    {logo: "./images/c++-logo.png", title: "C++", link: "https://github.com/Bosser16"},
    {logo: "./images/cs-logo.jpg", title: "C#", link: "https://github.com/Bosser16"}
];

const eduSection = document.getElementById("education");

education.forEach(x => {
    eduSection.innerHTML += 
    `<div class = "Ed-Card">
        <a href="${x.link}">
            <div class="Ed-Card-Title">
                <h1 class="Ed-Element">${x.degree}</h1>
                <p class="Ed-Element">${x.school}</p>
                <p class="Ed-Element">${x.year}</p>
            </div>
            <img src=${x.logo} alt="image failed" class="School-Logo"> 
        </a>
    </div>`;
});

const expSection = document.getElementById("experience");

jobs.forEach(y => {
    expSection.innerHTML += 
    `<div class = "Exp-Card">
        <img src="${y.logo}" class="Exp-Logo"> 
        <p class="Exp-Element">${y.title}</p>
        <p class="Exp-Element">${y.year}</p>
        <p class="Exp-Element">${y.description}</p>
    </div>`;
});

const techSection = document.getElementById("tech");

tech.forEach(k => {
    techSection.innerHTML += 
    `
    <div class="Tech-Backdrop">
        <p class="Tech-Hover-Title">Click to view examples</p>
            <div class="Tech-Card" style="background-image: url(${k.logo});">
                <div class="Tech-Title">
                    <span class="Tech-Element">${k.title}</span>
                </div>
            </div>
    </div>
    `;
});

