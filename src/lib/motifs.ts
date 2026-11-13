export const MOTIF_STROKE = 4.5;

const r1 = (n: number) => Math.round(n * 10) / 10;
const polar = (cx: number, cy: number, r: number, deg: number): [number, number] => {
  const a = (deg * Math.PI) / 180;
  return [r1(cx + r * Math.cos(a)), r1(cy + r * Math.sin(a))];
};
const arc = (cx: number, cy: number, r: number, from: number, to: number) => {
  const [x0, y0] = polar(cx, cy, r, from);
  const [x1, y1] = polar(cx, cy, r, to);
  return `<path d="M${x0} ${y0}A${r} ${r} 0 ${to - from > 180 ? 1 : 0} 1 ${x1} ${y1}"/>`;
};
const edge = (ax: number, ay: number, ar: number, bx: number, by: number, br: number) => {
  const d = Math.hypot(bx - ax, by - ay);
  const ux = (bx - ax) / d;
  const uy = (by - ay) / d;
  return `<path d="M${r1(ax + ux * ar)} ${r1(ay + uy * ar)}L${r1(bx - ux * br)} ${r1(by - uy * br)}"/>`;
};
const dot = (cx: number, cy: number, r = 6) =>
  `<circle cx="${cx}" cy="${cy}" r="${r}" fill="currentColor" stroke="none"/>`;
const ring = (cx: number, cy: number, r: number) => `<circle cx="${cx}" cy="${cy}" r="${r}"/>`;
const p = (d: string) => `<path d="${d}"/>`;
const rect = (x: number, y: number, w: number, h: number, rx = 0) =>
  `<rect x="${x}" y="${y}" width="${w}" height="${h}"${rx ? ` rx="${rx}"` : ""}/>`;

const network = () => {
  const out: [number, number][] = [-90, -30, 30, 90, 150, 210].map((a) => polar(200, 200, 126, a));
  const spokes = out.map(([x, y]) => edge(200, 200, 26, x, y, 15)).join("");
  const rim = [
    [0, 1],
    [1, 2],
    [3, 4],
    [4, 5],
    [5, 0],
  ]
    .map(([a, b]) => edge(out[a][0], out[a][1], 15, out[b][0], out[b][1], 15))
    .join("");
  return (
    ring(200, 200, 26) +
    out.map(([x, y]) => ring(x, y, 15)).join("") +
    spokes +
    rim +
    dot(200, 200, 7)
  );
};

const link = () => {
  const r = 84;
  const half = (Math.asin(10 / r) * 180) / Math.PI;
  const top = (Math.acos(44 / r) * 180) / Math.PI;
  return (
    arc(156, 200, r, -top + half, 360 - top - half) +
    arc(244, 200, r, 180 - top + half, 540 - top - half)
  );
};

const celtic = () => {
  const cy = 152;
  const h = 15;
  const bands = [68, 54]
    .map((r) => {
      const s = (Math.asin(h / r) * 180) / Math.PI;
      return [0, 90, 180, 270].map((q) => arc(200, cy, r, q + s, q + 90 - s)).join("");
    })
    .join("");
  return (
    p(
      `M${200 - h} 70H${200 + h}V${cy - h}H298V${cy + h}H${200 + h}V312H${200 - h}V${cy + h}H102V${cy - h}H${200 - h}Z`
    ) +
    bands +
    ring(200, cy, 7) +
    p("M164 312H236V334H164Z")
  );
};

const cycle = () => {
  const end = 250;
  const [tx, ty] = polar(200, 200, 112, end);
  const back = end - 90;
  const head = [back - 34, back + 34].map((a) => {
    const [x, y] = polar(tx, ty, 30, a);
    return `${x} ${y}`;
  });
  const ticks = Array.from({ length: 12 }, (_, i) => {
    const [x0, y0] = polar(200, 200, 80, i * 30);
    const [x1, y1] = polar(200, 200, i % 3 === 0 ? 94 : 88, i * 30);
    return p(`M${x0} ${y0}L${x1} ${y1}`);
  }).join("");
  return (
    arc(200, 200, 112, -66, end) +
    p(`M${head[0]}L${tx} ${ty}L${head[1]}`) +
    ticks +
    dot(200, 200, 7)
  );
};

const golden = () =>
  `<g transform="rotate(90 200 200)">` +
  rect(80, 126, 240, 148) +
  p("M228 126V274M228 218H320M264 218V274M228 238H264M248 218V238") +
  p(
    "M80 274A148 148 0 0 1 228 126A92 92 0 0 1 320 218A56 56 0 0 1 264 274A36 36 0 0 1 228 238A20 20 0 0 1 248 218"
  ) +
  `</g>`;

export const motifBodies: Record<string, string> = {
  code: p("M146 130L76 200L146 270") + p("M254 130L324 200L254 270") + p("M226 112L174 288"),

  patterns:
    rect(98, 98, 88, 88) +
    ring(258, 142, 46) +
    p("M142 214L192 302H92Z") +
    p("M258 210L306 258L258 306L210 258Z"),

  network: network(),

  db:
    `<ellipse cx="200" cy="112" rx="98" ry="30"/>` +
    p("M102 112V288A98 30 0 0 0 298 288V112") +
    p("M102 170A98 30 0 0 0 298 170") +
    p("M102 229A98 30 0 0 0 298 229") +
    dot(262, 166) +
    dot(262, 225) +
    dot(262, 284),

  scatter:
    p("M86 90V314H314") +
    p("M86 136H80M86 182H80M86 228H80M86 274H80M132 314V320M178 314V320M224 314V320M270 314V320") +
    p("M112 284L300 122") +
    [
      [124, 258],
      [146, 288],
      [170, 236],
      [196, 252],
      [214, 196],
      [240, 214],
      [260, 158],
      [286, 172],
      [292, 118],
    ]
      .map(([x, y]) => dot(x, y))
      .join(""),

  route:
    p("M116 302C80 252 80 236 80 214A36 36 0 0 1 152 214C152 236 152 252 116 302Z") +
    ring(116, 212, 12) +
    p("M284 196C248 146 248 130 248 108A36 36 0 0 1 320 108C320 130 320 146 284 196Z") +
    ring(284, 106, 12) +
    p("M130 318C210 334 300 300 290 216").replace("/>", ' stroke-dasharray="0 15"/>') +
    p("M96 318H136M264 212H304"),

  badge:
    rect(104, 92, 192, 236, 10) +
    p("M178 120H222") +
    ring(200, 182, 30) +
    p("M146 266C146 236 170 222 200 222C230 222 254 236 254 266") +
    p("M146 292H254M170 308H230"),

  cloud:
    p("M134 196A40 40 0 0 1 128 118A64 64 0 0 1 248 104A48 48 0 0 1 268 196Z") +
    p("M200 196V228") +
    rect(136, 228, 128, 40, 4) +
    rect(136, 276, 128, 40, 4) +
    dot(158, 248) +
    dot(158, 296) +
    p("M222 248H244M222 296H244"),

  shield:
    p("M200 80L304 114V198C304 262 262 304 200 330C138 304 96 262 96 198V114Z") +
    p("M200 98L288 127V198C288 252 252 288 200 310C148 288 112 252 112 198V127Z") +
    p("M190 207.3A20 20 0 1 1 210 207.3L218 252H182Z"),

  chat:
    p(
      "M114 104H286A18 18 0 0 1 304 122V234A18 18 0 0 1 286 252H190L134 302V252H114A18 18 0 0 1 96 234V122A18 18 0 0 1 114 104Z"
    ) +
    dot(154, 178, 9) +
    dot(200, 178, 9) +
    dot(246, 178, 9),

  target:
    ring(196, 204, 116) +
    ring(196, 204, 76) +
    ring(196, 204, 36) +
    dot(196, 204, 7) +
    p("M196 204L306 94") +
    p("M282 118V90M282 118H310M296 104V76M296 104H324"),

  briefcase:
    rect(90, 148, 220, 158, 8) +
    p("M162 148V126A12 12 0 0 1 174 114H226A12 12 0 0 1 238 126V148") +
    p("M90 210H178M222 210H310") +
    rect(178, 198, 44, 28, 3),

  compass:
    ring(200, 200, 126) +
    ring(200, 200, 110) +
    p("M200 90V104M200 296V310M90 200H104M296 200H310") +
    [45, 135, 225, 315]
      .map((a) => {
        const [x0, y0] = polar(200, 200, 110, a);
        const [x1, y1] = polar(200, 200, 102, a);
        return p(`M${x0} ${y0}L${x1} ${y1}`);
      })
      .join("") +
    p("M200 120L222 200L200 280L178 200Z") +
    p("M178 200H222") +
    ring(200, 200, 9),

  rocket:
    p("M200 76C246 118 256 184 248 252H152C144 184 154 118 200 76Z") +
    ring(200, 156, 22) +
    p("M152 212L116 262L154 256M248 212L284 262L246 256") +
    p("M174 252L180 272H220L226 252") +
    p("M188 290V314M200 290V330M212 290V314"),

  megaphone:
    rect(92, 166, 40, 68, 4) +
    p("M132 166L262 110V290L132 234") +
    p("M146 240L160 302H186L176 246") +
    p("M262 110C276 150 276 250 262 290") +
    p("M298 164A56 56 0 0 1 298 236M320 140A90 90 0 0 1 320 260"),

  chat2:
    p(
      "M168 208H150L108 242L120 208H102A14 14 0 0 1 88 194V114A14 14 0 0 1 102 100H234A14 14 0 0 1 248 114V176"
    ) +
    p(
      "M182 176H298A14 14 0 0 1 312 190V266A14 14 0 0 1 298 280H280L292 312L250 280H182A14 14 0 0 1 168 266V190A14 14 0 0 1 182 176Z"
    ) +
    p("M196 214H284M196 242H256") +
    p("M116 136H220M116 164H186"),

  growth:
    p("M84 312H316") +
    p("M100 312V262H148V312M176 312V224H224V312M252 312V182H300V312") +
    p("M100 222L176 172L222 186L300 104") +
    p("M262 104H300V142"),

  chart:
    p("M84 318H316") +
    [
      [108, 226, 300, 244, 284],
      [154, 200, 282, 218, 262],
      [200, 214, 290, 230, 272],
      [246, 150, 236, 166, 218],
      [292, 88, 186, 104, 164],
    ]
      .map(
        ([x, w0, w1, b0, b1]) =>
          p(`M${x} ${w0}V${b0}M${x} ${b1}V${w1}`) + rect(x - 15, b0, 30, b1 - b0, 1)
      )
      .join(""),

  bill:
    rect(74, 122, 252, 156, 4) +
    rect(90, 138, 220, 124, 2) +
    ring(200, 200, 40) +
    ring(200, 200, 28) +
    ring(122, 166, 10) +
    ring(278, 234, 10) +
    p("M118 236H156M244 164H282"),

  econ:
    p("M98 86V314H322") +
    p("M126 122L298 284") +
    p("M126 284L298 122") +
    p("M212 202V314M212 202H98").replace("/>", ' stroke-dasharray="0 12"/>') +
    dot(212, 202, 8),

  column:
    p("M108 86H292") +
    rect(118, 86, 164, 18, 0) +
    ring(134, 122, 13) +
    ring(266, 122, 13) +
    p("M147 122H253") +
    p("M134 109C150 104 250 104 266 109") +
    p("M156 136C152 186 152 236 158 290M244 136C248 186 248 236 242 290") +
    p("M178 140V286M200 140V286M222 140V286") +
    rect(144, 290, 112, 14, 0) +
    rect(128, 304, 144, 16, 0),

  hourglass:
    rect(110, 78, 180, 16, 3) +
    rect(110, 306, 180, 16, 3) +
    p("M124 94V306M276 94V306") +
    p("M146 94C146 152 194 172 194 200C194 228 146 248 146 306") +
    p("M254 94C254 152 206 172 206 200C206 228 254 248 254 306") +
    p("M164 146C186 154 214 154 236 146") +
    p("M200 206V258").replace("/>", ' stroke-dasharray="0 11"/>') +
    p("M158 306C170 278 186 266 200 266C214 266 230 278 242 306"),

  bulb:
    p("M166 262C166 236 134 218 134 172A66 66 0 1 1 266 172C266 218 234 236 234 262Z") +
    p("M168 282H232M174 300H226M188 318H212") +
    p("M182 262V218L191 202L200 218L209 202L218 218V262") +
    [-150, -120, -90, -60, -30]
      .map((a) => {
        const [x0, y0] = polar(200, 172, 88, a);
        const [x1, y1] = polar(200, 172, 106, a);
        return p(`M${x0} ${y0}L${x1} ${y1}`);
      })
      .join(""),

  puzzle: p(
    "M94 122H160A28 28 0 1 1 216 122H280V188A28 28 0 1 1 280 244V308H216A28 28 0 1 0 160 308H94V244A28 28 0 1 0 94 188Z"
  ),

  book:
    p("M200 122C170 100 128 94 90 102V282C128 274 170 280 200 302") +
    p("M200 122C230 100 272 94 310 102V282C272 274 230 280 200 302") +
    p("M200 122V302") +
    p("M90 282V296C128 288 170 294 200 316C230 294 272 288 310 296V282") +
    p(
      "M114 136C138 132 160 134 180 142M114 166C138 162 160 164 180 172M114 196C138 192 160 194 180 202M114 226C130 223 146 224 160 228"
    ) +
    p(
      "M220 142C240 134 262 132 286 136M220 172C240 164 262 162 286 166M220 202C240 194 262 192 286 196"
    ),

  flask:
    p("M172 84V174L98 296A14 14 0 0 0 110 318H290A14 14 0 0 0 302 296L228 174V84") +
    p("M158 84H242") +
    p("M172 112H188M172 138H188") +
    p("M134 242C156 232 176 252 200 242C224 232 244 252 266 242") +
    ring(178, 280, 9) +
    ring(220, 292, 6) +
    ring(232, 266, 5),

  pen:
    p("M200 326L148 222C142 196 154 160 168 140V92H232V140C246 160 258 196 252 222Z") +
    p("M168 140H232") +
    p("M168 116H232") +
    p("M200 326V214") +
    ring(200, 200, 12),

  golden: golden(),

  cycle: cycle(),

  link: link(),

  mountain:
    p("M64 304L152 172L190 226L240 132L336 304Z") +
    p("M219 170L230 184L242 170L254 184L262 172") +
    p("M248 192L310 304M253 232L293 304M258 270L277 304") +
    ring(126, 112, 22),

  hanger:
    p("M200 116A24 24 0 1 1 224 140C224 152 214 160 200 166") +
    p("M200 166L88 248A12 12 0 0 0 95 270H305A12 12 0 0 0 312 248Z"),

  checklist:
    rect(100, 100, 46, 46, 3) +
    rect(100, 177, 46, 46, 3) +
    rect(100, 254, 46, 46, 3) +
    p("M110 122L120 134L138 108M110 199L120 211L138 185") +
    p("M174 123H300M174 200H300M174 277H262"),

  pulse:
    p("M60 214H132L150 184L168 214H184L206 98L230 306L252 214H270L284 194L298 214H340") +
    p("M60 330H340").replace("/>", ' stroke-dasharray="0 14"/>'),

  scroll:
    p("M126 90H274A17 17 0 0 1 274 124H126A17 17 0 0 1 126 90Z") +
    p("M126 276H274A17 17 0 0 1 274 310H126A17 17 0 0 1 126 276Z") +
    p("M92 107H109M291 107H308M92 293H109M291 293H308") +
    p("M138 124V276M262 124V276") +
    p("M162 152H238M162 176H238M162 200H238M162 224H238M162 248H210"),

  celtic: celtic(),

  journal:
    rect(100, 74, 200, 258, 3) +
    p("M146 102H254") +
    p("M118 124H282M118 132H282") +
    rect(118, 152, 164, 82, 0) +
    p("M118 234L170 184L206 214L236 190L282 230") +
    p("M118 258H192M118 278H192M118 298H170M208 258H282M208 278H282M208 298H258"),

  org:
    rect(160, 86, 80, 54, 3) +
    rect(84, 260, 64, 50, 3) +
    rect(168, 260, 64, 50, 3) +
    rect(252, 260, 64, 50, 3) +
    p("M200 140V260M116 260V200H284V260"),

  board:
    rect(74, 90, 78, 220, 3) +
    rect(161, 90, 78, 220, 3) +
    rect(248, 90, 78, 220, 3) +
    p("M74 118H152M161 118H239M248 118H326") +
    rect(87, 132, 52, 34, 2) +
    rect(87, 178, 52, 34, 2) +
    rect(87, 224, 52, 34, 2) +
    rect(174, 132, 52, 34, 2) +
    rect(261, 132, 52, 34, 2) +
    rect(174, 178, 52, 34, 2).replace("/>", ' stroke-dasharray="0 10"/>') +
    rect(261, 178, 52, 34, 2) +
    p("M222 238H272M260 226L272 238L260 250"),

  sprout:
    p("M118 316H282") +
    p("M200 316C200 274 204 236 200 198") +
    p("M199 206C188 152 146 124 96 126C96 174 140 210 199 206Z") +
    p("M199 206C168 186 138 160 118 142") +
    p("M201 184C214 142 252 116 298 116C298 158 262 190 201 184Z") +
    p("M201 184C228 166 256 144 280 130"),

  shepherd:
    p("M118 330V156A56 56 0 0 1 230 156V168A12 12 0 0 1 218 180") +
    p(
      "M226 308C186 280 162 258 162 228A32 32 0 0 1 226 212A32 32 0 0 1 290 228C290 258 266 280 226 308Z"
    ),

  braces:
    p(
      "M172 84C142 84 136 102 136 128V164C136 186 128 196 104 200C128 204 136 214 136 236V272C136 298 142 316 172 316"
    ) +
    p(
      "M228 84C258 84 264 102 264 128V164C264 186 272 196 296 200C272 204 264 214 264 236V272C264 298 258 316 228 316"
    ) +
    dot(200, 200, 9),
};

export const motifLegends: Record<string, string> = {
  code: "Angle Brackets",
  patterns: "Four Figures",
  network: "Hub & Spokes",
  db: "The Data Store",
  scatter: "A Fitted Line",
  route: "From Here to There",
  badge: "The Name Badge",
  cloud: "Cloud over Rack",
  shield: "Shield & Keyhole",
  chat: "The Open Question",
  target: "Arrow in the Gold",
  briefcase: "The Briefcase",
  compass: "Compass Rose",
  rocket: "Lift-off",
  megaphone: "The Loud Hailer",
  chat2: "Call & Response",
  growth: "Rising Bars",
  chart: "Candlesticks",
  bill: "The Banknote",
  econ: "Supply Meets Demand",
  column: "Ionic Column",
  hourglass: "The Hourglass",
  bulb: "The Filament",
  puzzle: "The Missing Piece",
  book: "An Open Book",
  flask: "Erlenmeyer Flask",
  pen: "Fountain Nib",
  golden: "Golden Section",
  cycle: "The Daily Round",
  link: "Interlocked Rings",
  mountain: "Summit & Sun",
  hanger: "The Hanger",
  checklist: "Done, Done, Next",
  pulse: "Heartbeat",
  scroll: "The Scroll",
  celtic: "Celtic Cross",
  journal: "The Journal",
  org: "The Org Chart",
  board: "To Do, Doing, Done",
  sprout: "First Leaves",
  shepherd: "Crook & Heart",
  braces: "Curly Braces",
};

export const motifBounds: Record<string, [number, number, number, number]> = {
  code: [76, 112, 324, 288],
  patterns: [92, 96, 306, 306],
  network: [76, 59, 324, 341],
  db: [102, 82, 298, 318],
  scatter: [80, 90, 314, 320],
  route: [80, 72, 320, 322],
  badge: [104, 92, 296, 328],
  cloud: [99, 68, 297, 316],
  shield: [96, 80, 304, 330],
  chat: [96, 104, 304, 302],
  target: [80, 76, 324, 320],
  briefcase: [90, 114, 310, 306],
  compass: [74, 74, 326, 326],
  rocket: [116, 76, 284, 330],
  megaphone: [92, 110, 343, 302],
  chat2: [88, 100, 312, 312],
  growth: [84, 104, 316, 312],
  chart: [84, 88, 316, 318],
  bill: [74, 122, 326, 278],
  econ: [98, 86, 322, 314],
  column: [108, 86, 292, 320],
  hourglass: [110, 78, 290, 322],
  bulb: [108, 66, 292, 318],
  puzzle: [94, 94, 308, 308],
  book: [90, 99, 310, 316],
  flask: [95, 84, 305, 318],
  pen: [146, 92, 254, 326],
  golden: [126, 80, 274, 320],
  cycle: [88, 88, 312, 312],
  link: [72, 116, 328, 284],
  mountain: [64, 90, 336, 304],
  hanger: [83, 92, 317, 270],
  checklist: [100, 100, 300, 300],
  pulse: [60, 98, 340, 330],
  scroll: [92, 90, 308, 310],
  celtic: [102, 70, 298, 334],
  journal: [100, 74, 300, 332],
  org: [84, 86, 316, 310],
  board: [74, 90, 326, 310],
  sprout: [96, 116, 298, 316],
  shepherd: [118, 100, 291, 330],
  braces: [104, 84, 296, 316],
};

export interface MotifOptions {
  stroke?: number;
  className?: string;
  draw?: boolean;
  fit?: boolean;
}

const drawable = (body: string) =>
  body.replace(
    /<(path|circle|rect|ellipse)\b(?![^>]*stroke-dasharray)(?![^>]*stroke="none")/g,
    '<$1 pathLength="1"'
  );

export function motifSvg(name: string, opts: MotifOptions = {}): string {
  const raw = motifBodies[name];
  if (!raw) throw new Error(`unknown motif '${name}'`);
  const body = opts.draw ? drawable(raw) : raw;
  const cls = opts.className ? ` class="${opts.className}"` : "";
  const box = opts.fit ? motifBounds[name] : undefined;
  const pad = 8;
  const viewBox = box
    ? `${box[0] - pad} ${box[1] - pad} ${box[2] - box[0] + 2 * pad} ${box[3] - box[1] + 2 * pad}`
    : "0 0 400 400";
  return `<svg${cls} viewBox="${viewBox}" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="${opts.stroke ?? MOTIF_STROKE}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">${body}</svg>`;
}
