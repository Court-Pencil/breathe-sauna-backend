// Booking Calendar JavaScript
let selectedSaunaId = null

function selectSauna(card){
    selectedSaunaId = card.dataset.saunaId;
    document.getElementById('sauna-id').value = selectedSaunaId;

    document.querySelectorAll(".sauna-card").forEach(c => c.classList.remove("selected"));
    card.classList.add("selected");
    selectSauna()
    # reset BookingCalendar
}

function showCalendar(){
    const calendarDiv = document.getElementById('booking-calendar')
    calendarDiv.style.display = 'block';
}

function updateAvalibilty(){
    const slots = availableSlots[date][selectedSaunaId]
}


class BookingCalendar {
    constructor(availableSlots) {
        this.currentDate = new Date();
        this.selectedDate = null;
        this.selectedTimeSlot = null;
        this.allAvailableSlots = availableSlots;
        this.selectedSaunaId = null;
        
        this.init();
    }

    init() {
        this.renderCalendar();
        this.setupEventListeners();
    }

    renderCalendar() {
        const year = this.currentDate.getFullYear();
        const month = this.currentDate.getMonth();
        
        // Update month header
        document.getElementById('currentMonth').textContent = `${this.currentDate.toLocaleString('default', {month: 'long'})} ${year}`;

        // Get first day of month and total days
        const firstDay = new Date(year, month, 1);
        const lastDay = new Date(year, month + 1, 0);
        const totalDays = lastDay.getDate();
        
        // Adjust for Monday start
        let firstDayOfWeek = firstDay.getDay() - 1;
        if (firstDayOfWeek === -1) firstDayOfWeek = 6;

        // Get calendar grid
        const calendarGrid = document.querySelector('.calendar-grid');
        
        // Remove existing days
        const existingDays = calendarGrid.querySelectorAll('.day');
        existingDays.forEach(day => day.remove());

        // Add empty cells
        for (let i = 0; i < firstDayOfWeek; i++) {
            const emptyDay = document.createElement('div');
            emptyDay.className = 'day empty';
            calendarGrid.appendChild(emptyDay);
        }

        // Add days
        const today = new Date();
        today.setHours(0, 0, 0, 0);

        for (let day = 1; day <= totalDays; day++) {
            const dayElement = document.createElement('div');
            dayElement.className = 'day';
            dayElement.textContent = day;
            
            const currentDayDate = new Date(year, month, day);
            currentDayDate.setHours(0, 0, 0, 0);
            
            if (currentDayDate.getTime() === today.getTime()) {
                dayElement.classList.add('today');
            }
            
            if (currentDayDate < today) {
                dayElement.classList.add('past');
            } else {
                dayElement.addEventListener('click', () => this.selectDate(dayElement, year, month, day));
            }
            
            calendarGrid.appendChild(dayElement);
        }
    }

    selectDate(e, year, month, day) {
        this.selectedDate = new Date(year, month, day);
        
        // Update styling
        document.querySelectorAll('.day').forEach(d => d.classList.remove('selected'));
        e.classList.add('selected');
        
        // Show time slots
        this.showTimeSlots();
    }

    showTimeSlots() {
        const timeSlotsSection = document.getElementById('timeSlotsSection');
        const selectedDateHeader = document.getElementById('selectedDateHeader');
        const timeSlotsGrid = document.getElementById('timeSlotsGrid');
        
        // Format date
        const options = { weekday: 'long', month: 'long', day: 'numeric' };
        selectedDateHeader.textContent = this.selectedDate.toLocaleDateString('en-gb', options);
        
        // Get slots for this date
        const dateKey = this.selectedDate.toISOString().split('T')[0];
        const slots = this.availableSlots[dateKey] || [];
        
        // Clear existing
        timeSlotsGrid.innerHTML = '';
        
        if (slots.length === 0) {
            timeSlotsGrid.innerHTML = '<div class="no-slots-message">No available time slots for this date</div>';
        } else {
            slots.forEach(slot => {
                const slotElement = document.createElement('div');
                slotElement.className = 'time-slot';
                
                if (slot.available <= 0) {
                    slotElement.classList.add('disabled');
                }
                
                slotElement.innerHTML = `
                    <div class="time-slot-time">${slot.time}</div>
                    <div class="time-slot-availability">
                        ${slot.available > 0 ? `${slot.available} spot${slot.available > 1 ? 's' : ''} left` : 'Fully booked'}
                    </div>
                `;
                
                if (slot.available > 0) {
                    slotElement.addEventListener('click', () => this.selectTimeSlot(slot, slotElement));
                }
                
                timeSlotsGrid.appendChild(slotElement);
            });
        }
        
        timeSlotsSection.style.display = 'block';
        this.selectedTimeSlot = null;
        document.getElementById('confirmBtn').disabled = true;
    }

    selectTimeSlot(slot, element) {
        document.querySelectorAll('.time-slot').forEach(s => s.classList.remove('selected'));
        element.classList.add('selected');
        this.selectedTimeSlot = slot;
        document.getElementById('confirmBtn').disabled = false;
    }

    setupEventListeners() {
        document.getElementById('prevMonth').addEventListener('click', () => {
            this.currentDate.setMonth(this.currentDate.getMonth() - 1);
            this.renderCalendar();
        });

        document.getElementById('nextMonth').addEventListener('click', () => {
            this.currentDate.setMonth(this.currentDate.getMonth() + 1);
            this.renderCalendar();
        });

        document.getElementById('cancelBtn').addEventListener('click', () => {
            document.getElementById('timeSlotsSection').style.display = 'none';
            document.querySelectorAll('.day').forEach(d => d.classList.remove('selected'));
            this.selectedDate = null;
            this.selectedTimeSlot = null;
        });

        document.getElementById('confirmBtn').addEventListener('click', () => {
            if (this.selectedDate && this.selectedTimeSlot) {
                // Set form values
                document.getElementById('id_booking_date').value = this.selectedDate.toISOString().split('T')[0];
                document.getElementById('id_time_slot').value = this.selectedTimeSlot.id;
                
                // Submit form
                document.getElementById('bookingForm').submit();
            }
        });
    }
}