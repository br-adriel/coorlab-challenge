export function timeStringToHours(timeString) {
  const [hours, min, sec] = timeString.split(':');

  if (min >= 30) return `${parseInt(hours)}.5h`;
  return parseInt(hours) + 'h';
}
