export const icons = {
  guide: '<circle cx="12" cy="12" r="8.5"/><path d="m15.4 8.6-2.3 4.5-4.5 2.3 2.3-4.5Z"/>',
  concepts:
    '<circle cx="6" cy="7" r="2.25"/><circle cx="18" cy="7" r="2.25"/><circle cx="12" cy="17" r="2.25"/><path d="M8.25 7h7.5M7.16 8.93l3.68 6.14M16.84 8.93l-3.68 6.14"/>',
  problems:
    '<path d="M6 3.75h8.5l3.5 3.5v13H6Z"/><path d="M14.5 3.75v3.5H18M9 11.5h6M9 15h6M9 18.5h3.5"/>',
  check: '<path d="M4.75 4.75h14.5v14.5H4.75Z"/><path d="m8.5 12.25 2.4 2.4 4.6-5"/>',
  search: '<circle cx="10.5" cy="10.5" r="6"/><path d="m15 15 5 5"/>',
  library:
    '<path d="M3.5 20.25h17"/><path d="M5.25 20.25V6.75h3.5v13.5M10.25 20.25V4.25h3.5v16M15.25 20.25V8.75h3.5v11.5"/><path d="M5.25 10h3.5M10.25 7.5h3.5M15.25 12h3.5"/>',
  handbook:
    '<path d="M6.75 3.75h11.5v16.5H6.75a2 2 0 0 1-2-2V5.75a2 2 0 0 1 2-2Z"/><path d="M8.25 3.75v16.5M12.5 3.75v6.5l1.75-1.4 1.75 1.4v-6.5"/>',
  archive: '<path d="M4.75 4.25h14.5v15.5H4.75ZM4.75 12h14.5"/><path d="M10 8.1h4M10 15.9h4"/>',
  bookmark: '<path d="M7 4.25h10v15.5l-5-3.5-5 3.5Z"/>',
  "arrow-left": '<path d="M19 12H5M10.5 6.5 5 12l5.5 5.5"/>',
  "arrow-right": '<path d="M5 12h14M13.5 6.5 19 12l-5.5 5.5"/>',
  "arrow-up-right": '<path d="M7.5 16.5 16.5 7.5M9 7.5h7.5V15"/>',
  "chevron-left": '<path d="M14.5 6 8.5 12l6 6"/>',
  "chevron-right": '<path d="m9.5 6 6 6-6 6"/>',
  sun: '<circle cx="12" cy="12" r="3.75"/><path d="M12 2.75v2M12 19.25v2M2.75 12h2M19.25 12h2M5.46 5.46l1.41 1.41M17.13 17.13l1.41 1.41M18.54 5.46l-1.41 1.41M6.87 17.13l-1.41 1.41"/>',
  moon: '<path d="M19.5 14.6A7.75 7.75 0 0 1 9.4 4.5a7.75 7.75 0 1 0 10.1 10.1Z"/>',
  checkup: '<path d="M3 12.5h4l2.25-5.5 4.5 11 2.25-5.5H21"/>',
  enrich: '<path d="m14.75 4.75 4.5 4.5L9 19.5H4.5V15Z"/><path d="m12.5 7 4.5 4.5"/>',
  plus: '<path d="M12 5v14M5 12h14"/>',
  minus: '<path d="M5 12h14"/>',
  copy: '<path d="M8.75 8.75h10.5v10.5H8.75Z"/><path d="M15.25 8.75v-4H4.75v10.5h4"/>',
  close: '<path d="m6 6 12 12M18 6 6 18"/>',
} as const;

export type IconName = keyof typeof icons;

export function isIconName(name: string): name is IconName {
  return Object.prototype.hasOwnProperty.call(icons, name);
}
