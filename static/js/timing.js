const met_time = new Date(2022, 10, 26, 19, 26)
const together_time = new Date(2023, 1, 17, 20)
let flags = {
    met_hundred: 0,
    met_years: 0,
    together_hundred: 0,
    together_years: 0,
}

function insert_hundred(days){
    let days_hundreds = days.cloneNode(true)
    days_hundreds.removeAttribute('data-days-tens');
    days_hundreds.setAttribute('data-days-hundreds', null)
    days_hundreds.childNodes

    days_hundreds.setAttribute('class', 'flip-card')
    days_hundreds.setAttribute('data-days-hundreds', null)

    days.parentNode.insertBefore(days_hundreds, days_tens)
}
flags = new Proxy(flags, {
    set(target, p, value, receiver) {
        target[p] = value;
        // 如果设置的是天数(几百天)
        if (p === 'met_hundred' && flags[p] > 0) {
            let days_tens = document.querySelector('.met-time .days [data-days-tens]');
            insert_hundred(days_tens)
        }
        // 如果设置的是几年
        if (p === 'met_years' && flags[p] > 0) {
            let years_ele = document.querySelector(".met-time .years")
            years_ele.setAttribute('style', 'display: flex')
            flip(document.querySelector('[data-years-tens]'), Math.floor(flags['years'] / 10))
            flip(document.querySelector('[data-years-ones]'), Math.floor(flags['years'] % 10))
        }
        // 如果设置的是天数(几百天)
        if (p === 'together_hundred' && flags[p] > 0) {
            let days_tens = document.querySelector('.together-time .days [data-days-tens]');
            insert_hundred(days_tens)
        }
        // 如果设置的是几年
        if (p === 'together_years' && flags[p] > 0) {
            let years_ele = document.querySelector(".together-time .years")
            years_ele.setAttribute('style', 'display: flex')
            flip(document.querySelector('[data-years-tens]'), Math.floor(flags['years'] / 10))
            flip(document.querySelector('[data-years-ones]'), Math.floor(flags['years'] % 10))
        }
    }

})
setInterval(() => {
    const currentDate = new Date()
    // 如果日期超过 1 年
    let met_years = currentDate.getFullYear() - met_time.getFullYear()
    let tmp_met_date = currentDate.setFullYear(met_time.getFullYear()) - met_time
    if (tmp_met_date < 0){
        currentDate.setFullYear(met_time.getFullYear() + 1)
        met_years = met_years - 1;
    }
    if (met_years) flags['met_years'] = met_years
    const between_met_time = Math.ceil((currentDate - met_time) / 1000)
    flipAllCards('met-time', between_met_time)
    // 如果日期超过 1 年
    let together_years = currentDate.getFullYear() - together_time.getFullYear()
    let tmp_together_date = currentDate.setFullYear(together_time.getFullYear()) - together_time
    if (tmp_together_date < 0){
        currentDate.setFullYear(together_time.getFullYear() + 1)
        together_years = together_years - 1;
    }
    if (together_years) flags['together_years'] = together_years
    const between_together_time = Math.ceil((currentDate - together_time) / 1000)
    flipAllCards('together-time', between_together_time)
}, 1000)

function flipAllCards(selector, time) {
    const seconds = time % 60
    const minutes = Math.floor(time / 60) % 60
    const hours = Math.floor(time / 3600) % 24
    const days = Math.floor(time / (3600 * 24))
    const hundred = Math.floor(days / 100)
    // 如果天数超过 100 天
    if (days > 100 && selector === 'met-time' && hundred - flags['met_hundred']) {
        flags['met_hundred'] = hundred;
    }

    if (days > 100 && selector === 'together' && hundred - flags['met_hundred']) {
        flags['met_hundred'] = hundred;
    }


    flip(selector, document.querySelector(`.${selector} [data-days-hundreds]`), Math.floor(days / 100))
    flip(selector, document.querySelector(`.${selector} [data-days-tens]`), Math.floor(days / 10 % 10 ))
    flip(selector, document.querySelector(`.${selector} [data-days-ones]`), days %  10)
    flip(selector, document.querySelector(`.${selector} [data-hours-tens]`), Math.floor(hours / 10))
    flip(selector, document.querySelector(`.${selector} [data-hours-ones]`), hours % 10)
    flip(selector, document.querySelector(`.${selector} [data-minutes-tens]`), Math.floor(minutes / 10))
    flip(selector, document.querySelector(`.${selector} [data-minutes-ones]`), minutes % 10)
    flip(selector, document.querySelector(`.${selector} [data-seconds-tens]`), Math.floor(seconds / 10))
    flip(selector, document.querySelector(`.${selector} [data-seconds-ones]`), seconds % 10)
}

function flip(selector, flipCard, newNumber) {
    if (flipCard) {
        const topHalf = flipCard.querySelector(`.${selector} .top`)
        const startNumber = parseInt(topHalf.textContent)
        if (newNumber === startNumber) return

        const bottomHalf = flipCard.querySelector(`.${selector} .bottom`)
        const topFlip = document.createElement('div')
        topFlip.classList.add('top-flip')
        const bottomFlip = document.createElement('div')
        bottomFlip.classList.add('bottom-flip')

        // top.textContent = startNumber
        bottomHalf.textContent = startNumber
        topFlip.textContent = startNumber
        bottomFlip.textContent = newNumber

        topFlip.addEventListener('animationstart', e => {
            topHalf.textContent = newNumber
        })
        topFlip.addEventListener('animationend', e => {
            topFlip.remove()
        })
        bottomFlip.addEventListener('animationend', e => {
            bottomHalf.textContent = newNumber
            bottomFlip.remove()
        })
        flipCard.append(topFlip, bottomFlip)
    }
}