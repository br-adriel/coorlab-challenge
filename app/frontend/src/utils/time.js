export function timeStringToHours(timeString) {
  const [hours, min, sec] = timeString.split(':');

  if (min >= 30) return `${hours}.5h`;
  else return hours + 'h';
}
