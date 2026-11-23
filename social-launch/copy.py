import json, re
FOOT = "Adams Welding ~ Millwright ~ Crane | Harrisburg, AR\n📞 Call/Text (870) 408-0221 · Rig Trucks On Call 24/7"
C = {}
C['ig_name'] = ("Adams Welding | Grain & Crane", 30)
C['ig_bio'] = ("Grain systems · Certified welding · Millwright · 40-ton crane\nHarrisburg, AR · NE Arkansas & the Mid-South\n📞 Rig trucks on call 24/7 · (870) 408-0221", 150)
C['th_bio'] = ("Welders, millwrights & a crane crew out of Harrisburg, AR. Grain bins to structural steel to 40-ton lifts. Talking shop here. 📞 (870) 408-0221", 150)
C['x_name'] = ("Adams Welding, Millwright & Crane", 50)
C['x_bio'] = ("Grain systems, certified welding (AWS D1.1/D1.2), millwright crews & our own 40-ton crane. Harrisburg, AR. Rig trucks on call 24/7 · (870) 408-0221", 160)
C['tt_name'] = ("Adams Welding & Crane", 30)
C['tt_bio'] = ("Bins. Beads. Bearings. Booms. 🔥 Welding & crane crew out of Harrisburg, AR", 80)
C['yt_name'] = ("Adams Welding, Millwright & Crane", 100)
C['yt_desc'] = ("""Adams Welding, Millwright & Crane Services is a family-owned shop out of Harrisburg, Arkansas. We build and fix grain systems, do certified welding, send millwright crews, and run our own 40-ton crane with an NCCCO-certified operator.

Bins. Beads. Bearings. Booms.
👉 Grain systems: bins built and repaired, loop systems, sweeps and unloads, bucket elevators and spouting, aeration floors and fans, grain dryers
👉 Certified welding: AWS D1.1 structural and D1.2 aluminum, pipe and gas lines, TIG stainless and aluminum, mobile rig trucks on call 24/7
👉 Millwright: bearings, gearboxes, drives, motors and shutdown crews
👉 Crane & rigging: our own 40-ton crane, certified rigger, 90-ton available for bigger lifts

Working all over NE Arkansas and the Mid-South. Licensed, bonded & insured.

Call/Text (870) 408-0221
office@adamswelding.net
adamswelding.net""", 1000)
C['nd_desc'] = ("Family-owned welding, millwright and crane outfit in Harrisburg. Mobile rig trucks on call 24/7 for farm equipment, trailers, gates and handrails. Certified structural, pipe, stainless and aluminum welders. Grain bins built and repaired. Licensed, bonded & insured. Call/Text (870) 408-0221.", 500)

HT1 = "#AdamsWelding #Welding #Millwright #CraneService #GrainBins #GrainHandling #ArkansasAg #NEArkansas #Jonesboro #CertifiedWelder"
C['ig_cap1'] = (f"""Bins. Beads. Bearings. Booms. That's the whole shop in four words.

Adams Welding is on Instagram. Here's what we do:

👉 Bins: grain systems, from new bins and loops to sweeps, legs and aeration floors
👉 Beads: certified welding, AWS D1.1 structural and D1.2 aluminum, pipe, TIG stainless and aluminum
👉 Bearings: millwright crews for bearings, gearboxes, drives and shutdowns
👉 Booms: our own 40-ton crane with an NCCCO-certified operator

Follow along for real jobs, straight from the crew. Got something broke? Call or text.

{FOOT}

{HT1}""", 2200)
HT2 = "#AdamsWelding #GrainSystems #Millwright #CraneAndRigging #StructuralWelding #PipeWelding #RiceMill #GrainElevator #ArkansasAg #MidSouth"
C['ig_cap2'] = (f"""Four trades. One call. Grain, welding, millwright and crane work from one outfit in Harrisburg.

Most jobs on a grain site or in a plant need more than one trade. The leg needs a new head shaft, the shaft needs a crane to get it up there, and the new spout needs welding. We do all of it, so you make one call instead of four.

👉 Grain systems: bins, loops, sweeps, legs, spouting, aeration, dryers
👉 Certified welding: structural, pipe, TIG stainless and aluminum, 24/7 mobile
👉 Millwright: bearings, gearboxes, drives, motors, shutdown crews
👉 Crane & rigging: our own 40-ton crane, NCCCO operator, certified rigger

Save this for the next time something breaks.

{FOOT}

{HT2}""", 2200)
HT3 = "#AdamsWelding #MobileWelding #RigTruck #FarmRepair #AgWelding #GrainCart #Harrisburg #Jonesboro #NEArkansas #Bootheel"
C['ig_cap3'] = (f"""Broke down at 2 AM? The rig trucks are on call 24/7.

A grain cart tongue snaps mid-harvest. A gate operator quits on a Sunday. A loop chain lets go right before the trucks roll in. That's what the rig trucks are for.

Certified structural, pipe, stainless and aluminum welders. Licensed, bonded & insured, with $3 million insurance plus workers' comp. Based in Harrisburg, working all over NE Arkansas and the Mid-South.

Save the number. You'll want it at the worst possible time.

{FOOT}

{HT3}""", 2200)
C['th_post1'] = ("Adams Welding is on Threads. We're welders, millwrights and a crane crew out of Harrisburg, Arkansas: grain bins, certified welding, bearings and gearboxes, and our own 40-ton crane.\n\nBins. Beads. Bearings. Booms.\n\nAsk us anything about keeping steel and grain moving.", 500)
C['th_post2'] = ("Question for the farmers and plant folks: what's the one piece of equipment that always seems to break at the worst possible time?\n\nOn a lot of grain sites it's a leg bearing or the loop chain, right when the trucks start rolling. What's yours?", 500)
C['x_pin'] = ("Adams Welding is on X.\n\nGrain systems, certified welding, millwright crews and our own 40-ton crane, out of Harrisburg, AR. Rig trucks on call 24/7.\n\nCall/text (870) 408-0221\nhttps://adamswelding.net", 280)
C['x_post2'] = ("Bins. Beads. Bearings. Booms.\n\nFour trades, one call. Grain systems, certified welding, millwright and crane, all from one outfit in NE Arkansas. #Welding #Arkansas", 280)
C['tt_caption'] = ("Bins. Beads. Bearings. Booms. 🔥 Welding, millwright & crane out of Harrisburg, AR. Call/Text 870-408-0221 #welding #millwright #crane #grainbins #arkansas", 2200)
C['xpromo'] = ("""Same crew, same work, more places to see it.

Adams Welding is now on Instagram, Threads, X, TikTok and YouTube. Follow along for real jobs straight from the crew: grain systems, certified welding, millwright work and crane lifts.

Search "Adams Welding" or tap through:
👉 Instagram & Threads: @adamswelding
👉 X: @adamswelding
👉 TikTok: @adamswelding
👉 YouTube: @adamswelding

""" + FOOT + "\n\n#AdamsWelding #SupportLocal", 2200)

def xlen(t):
    # X counts every URL as 23 chars and emoji as 2
    t2 = re.sub(r'https?://\S+', 'x'*23, t)
    n = 0
    for ch in t2:
        n += 2 if ord(ch) > 0x2FFF else 1
    return n
bad = False
for k,(t,lim) in C.items():
    n = xlen(t) if k.startswith('x_') else len(t)
    words = len(re.findall(r"[A-Za-z0-9$'’/.-]+", t.split('#')[0]))
    flag = 'OK ' if n <= lim else 'OVER'
    if n > lim: bad = True
    extra = f" hook={len(t.splitlines()[0])}" if k.startswith('ig_cap') else ''
    print(f"{flag} {k:10s} {n:4d}/{lim}  words~{words}{extra}")
json.dump({k:v[0] for k,v in C.items()}, open('copy.json','w'), ensure_ascii=False, indent=1)
banned = ["excited to announce","thrilled","solutions","leverage","synergy","world-class","reach out","don't hesitate","elevate","game-changer","unlock","myshopify"]
for k,(t,_) in C.items():
    for b in banned:
        if b in t.lower(): print("BANNED", k, b)
