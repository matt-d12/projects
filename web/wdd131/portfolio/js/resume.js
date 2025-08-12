import { resume } from './resumedata.mjs';

function createSection(title, items) {
  const section = document.createElement('section');
  const h2 = document.createElement('h2');
  h2.textContent = title;
  section.appendChild(h2);

  items.forEach(entry => {
    const div = document.createElement('div');
    div.classList.add('resume-entry');

    const titleLine = `<h3>${entry.title} <span>${entry.date}</span></h3>`;
    const subtitle = entry.company || entry.school ? `<h4>${entry.company || entry.school}</h4>` : '';
    const bullets = entry.details.map(item => `<li>${item}</li>`).join('');

    div.innerHTML = `${titleLine}${subtitle}<ul>${bullets}</ul>`;
    section.appendChild(div);
  });

  return section;
}

function createSkillsSection(skills, title) {
  const section = document.createElement('section');
  section.innerHTML = `<h2>${title}</h2>`;

  Object.entries(skills).forEach(([category, items]) => {
    const div = document.createElement('div');
    div.classList.add('resume-skill');
    div.innerHTML = `<h4>${category}</h4><p>${items.join(', ')}</p>`;
    section.appendChild(div);
  });

  return section;
}

function renderResume() {
  const container = document.getElementById('resume');

  if (!container) {
    console.error("No #resume element found.");
    return;
  }

  // Contact Info
  const contact = document.createElement('div');
  contact.className = 'contact';
  contact.innerHTML = `
    <h1>${resume.contact.name}</h1>
    <p><a href="mailto:${resume.contact.email}">${resume.contact.email}</a> | 
    <a href="${resume.contact.linkedin}" target="_blank">LinkedIn</a> | 
    ${resume.contact.phone}</p>
  `;
  container.appendChild(contact);

  container.appendChild(createSection('Relevant Experience', resume.experience));
  container.appendChild(createSection('Education & Accolades', resume.education));

  const skillsTitle = document.createElement('h2');
  skillsTitle.textContent = 'Skills & Tools';
  container.appendChild(skillsTitle);

  container.appendChild(createSkillsSection(resume.skills.learning, 'Currently Learning'));
  container.appendChild(createSkillsSection(resume.skills.proficient, 'Proficient With'));
}

document.addEventListener('DOMContentLoaded', renderResume);