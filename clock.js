function updateClock() {
    const now = new Date();
    let hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    const ampm = hours >= 12 ? 'PM' : 'AM';
  
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
  
    const strHours = hours.toString().padStart(2, '0');
    const strMinutes = minutes.toString().padStart(2, '0');
    const strSeconds = seconds.toString().padStart(2, '0');
  
    document.querySelector('.hr').textContent = strHours;
    document.querySelector('.min').textContent = strMinutes;
    document.querySelector('.sec').textContent = strSeconds;
    document.querySelector('.time-zon').textContent = ampm;
  }
  
  // Initial call to set the clock immediately
  updateClock();
  
  // Update the clock every second
  setInterval(updateClock, 1000);

  

  