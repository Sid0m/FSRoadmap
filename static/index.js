document.querySelectorAll('.toggle-btn').forEach(button => {
  button.addEventListener('click', function () {
    const parentContent = this.closest('.timeline-content');
    const content = parentContent.querySelector('p');; // Der nächste Bruder ist das <p>-Element

    // Toggle the "active" class to expand/collapse the content
    if (content) {
      content.classList.toggle('active');
      parentContent.classList.toggle('active');

      
      if (content.classList.contains('active')) {
        parentContent.style.maxHeight = parentContent.scrollHeight + "px";
      } else {
        parentContent.style.maxHeight = "50";
      }

      // Ändere den Button-Text und rotiere den Pfeil
      const arrow = this.querySelector('.arrow');
      arrow.style.transform = parentContent.classList.contains('active') ? 'rotate(180deg)' : 'rotate(0deg)';
    }
  });
});  