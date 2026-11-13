export const icons = {
  "arrow-left": '<path d="M19 12H5M10.5 6.5 5 12l5.5 5.5"/>',
  "arrow-right": '<path d="M5 12h14M13.5 6.5 19 12l-5.5 5.5"/>',
  "arrow-up-right": '<path d="M7.5 16.5 16.5 7.5M9 7.5h7.5V15"/>',
  "chevron-right": '<path d="m9.5 6 6 6-6 6"/>',
  checkup: '<path d="M3 12.5h4l2.25-5.5 4.5 11 2.25-5.5H21"/>',
  enrich: '<path d="m14.75 4.75 4.5 4.5L9 19.5H4.5V15Z"/><path d="m12.5 7 4.5 4.5"/>',
  plus: '<path d="M12 5v14M5 12h14"/>',
  minus: '<path d="M5 12h14"/>',
  copy: '<path d="M8.75 8.75h10.5v10.5H8.75Z"/><path d="M15.25 8.75v-4H4.75v10.5h4"/>',
} as const;

export type IconName = keyof typeof icons;

export function isIconName(name: string): name is IconName {
  return Object.prototype.hasOwnProperty.call(icons, name);
}
