#!/usr/bin/env python3
"""Script to inject audio comparison section into index.html"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS to inject (before </style></head>)
css_code = '''
/* Audio Comparison Section Styles */
.section_audio-compare {
  background: linear-gradient(180deg, #0a0a0a 0%, #111111 50%, #0a0a0a 100%);
  padding: 6rem 0;
  position: relative;
  overflow: hidden;
}

.section_audio-compare::before {
  content: "";
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 400px;
  background: radial-gradient(circle, rgba(236, 224, 72, 0.08) 0%, transparent 70%);
  pointer-events: none;
}

.audio-compare_component {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  text-align: center;
}

.audio-compare_heading {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 700;
  color: #ece048;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.audio-compare_subheading {
  font-size: clamp(1rem, 2vw, 1.25rem);
  color: rgba(255, 255, 255, 0.7);
  max-width: 700px;
  margin: 0 auto 3rem auto;
  line-height: 1.6;
}

.audio-cards_wrapper {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.audio-card {
  background: linear-gradient(145deg, rgba(30, 30, 30, 0.9) 0%, rgba(20, 20, 20, 0.95) 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 2rem;
  position: relative;
  transition: all 0.3s ease;
}

.audio-card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 20px;
  padding: 1px;
  background: linear-gradient(145deg, rgba(236, 224, 72, 0.3), transparent);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.audio-card:hover {
  transform: translateY(-5px);
  border-color: rgba(236, 224, 72, 0.3);
}

.audio-card_title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #fff;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.audio-card_title span {
  color: #ece048;
}

.audio-player {
  background: rgba(0, 0, 0, 0.4);
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1rem;
}

.audio-player:last-child {
  margin-bottom: 0;
}

.audio-player_label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  margin-bottom: 0.75rem;
  font-weight: 600;
  text-align: left;
}

.audio-player_label.before {
  color: rgba(255, 255, 255, 0.5);
}

.audio-player_label.after {
  color: #ece048;
}

.audio-player_controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.play-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(145deg, #ece048, #d4c940);
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.play-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 0 20px rgba(236, 224, 72, 0.4);
}

.play-btn svg {
  width: 20px;
  height: 20px;
  fill: #000;
  margin-left: 2px;
}

.play-btn.playing svg {
  margin-left: 0;
}

.waveform-container {
  flex: 1;
  height: 50px;
  position: relative;
  cursor: pointer;
}

.waveform {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  gap: 2px;
}

.waveform-bar {
  flex: 1;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 2px;
  transition: background 0.1s ease;
  min-width: 3px;
  max-width: 6px;
}

.waveform-bar.active {
  background: linear-gradient(180deg, #ece048, #d4c940);
}

.audio-time {
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.6);
  font-family: monospace;
  min-width: 45px;
  text-align: right;
}

.audio-compare_cta {
  font-size: 1.125rem;
  color: rgba(255, 255, 255, 0.8);
  font-style: italic;
}

.audio-compare_cta strong {
  color: #ece048;
  font-style: normal;
}

@media screen and (max-width: 767px) {
  .section_audio-compare {
    padding: 4rem 0;
  }
  
  .audio-cards_wrapper {
    grid-template-columns: 1fr;
  }
  
  .audio-card {
    padding: 1.5rem;
  }
  
  .audio-player_controls {
    gap: 0.75rem;
  }
  
  .play-btn {
    width: 44px;
    height: 44px;
  }
  
  .waveform-container {
    height: 40px;
  }
}
/* End Audio Section Styles */

'''

# HTML section to inject (between curriculum and success sections)
html_section = '''
<!-- Audio Before/After Comparison Section -->
<section class="section_audio-compare">
  <div class="audio-compare_component">
    <h2 class="audio-compare_heading">Hear The Difference For Yourself</h2>
    <p class="audio-compare_subheading">Raw talent meets professional polish. Listen to real before &amp; after transformations created using the exact techniques taught in this course.</p>
    
    <div class="audio-cards_wrapper">
      <!-- Singer Card -->
      <div class="audio-card">
        <h3 class="audio-card_title">Vocal Processing — <span>Singer</span></h3>
        
        <div class="audio-player" data-audio="singer-before">
          <div class="audio-player_label before">Before</div>
          <div class="audio-player_controls">
            <button class="play-btn" aria-label="Play">
              <svg class="play-icon" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              <svg class="pause-icon" style="display:none" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
            <div class="waveform-container">
              <div class="waveform"></div>
            </div>
            <span class="audio-time">0:00</span>
          </div>
          <audio src="assets/audio/singer-before.mp3" preload="metadata"></audio>
        </div>
        
        <div class="audio-player" data-audio="singer-after">
          <div class="audio-player_label after">After</div>
          <div class="audio-player_controls">
            <button class="play-btn" aria-label="Play">
              <svg class="play-icon" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              <svg class="pause-icon" style="display:none" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
            <div class="waveform-container">
              <div class="waveform"></div>
            </div>
            <span class="audio-time">0:00</span>
          </div>
          <audio src="assets/audio/singer-after.mp3" preload="metadata"></audio>
        </div>
      </div>
      
      <!-- Rap Card -->
      <div class="audio-card">
        <h3 class="audio-card_title">Vocal Processing — <span>Rap</span></h3>
        
        <div class="audio-player" data-audio="rap-before">
          <div class="audio-player_label before">Before</div>
          <div class="audio-player_controls">
            <button class="play-btn" aria-label="Play">
              <svg class="play-icon" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              <svg class="pause-icon" style="display:none" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
            <div class="waveform-container">
              <div class="waveform"></div>
            </div>
            <span class="audio-time">0:00</span>
          </div>
          <audio src="assets/audio/rap-before.mp3" preload="metadata"></audio>
        </div>
        
        <div class="audio-player" data-audio="rap-after">
          <div class="audio-player_label after">After</div>
          <div class="audio-player_controls">
            <button class="play-btn" aria-label="Play">
              <svg class="play-icon" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              <svg class="pause-icon" style="display:none" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
            <div class="waveform-container">
              <div class="waveform"></div>
            </div>
            <span class="audio-time">0:00</span>
          </div>
          <audio src="assets/audio/rap-after.mp3" preload="metadata"></audio>
        </div>
      </div>
    </div>
    
    <p class="audio-compare_cta">This is what proper vocal processing sounds like. <strong>And this is exactly what you'll learn to do.</strong></p>
  </div>
</section>

'''

# JavaScript to inject (before </body>)
js_code = '''
<!-- Audio Player JavaScript -->
<script>
(function() {
  // Generate waveform bars
  document.querySelectorAll('.waveform').forEach(waveform => {
    const barCount = 40;
    for (let i = 0; i < barCount; i++) {
      const bar = document.createElement('div');
      bar.className = 'waveform-bar';
      // Random heights for visual interest
      const height = 20 + Math.random() * 80;
      bar.style.height = height + '%';
      waveform.appendChild(bar);
    }
  });

  // Audio player functionality
  document.querySelectorAll('.audio-player').forEach(player => {
    const audio = player.querySelector('audio');
    const playBtn = player.querySelector('.play-btn');
    const playIcon = player.querySelector('.play-icon');
    const pauseIcon = player.querySelector('.pause-icon');
    const waveformContainer = player.querySelector('.waveform-container');
    const waveformBars = player.querySelectorAll('.waveform-bar');
    const timeDisplay = player.querySelector('.audio-time');

    if (!audio) return;

    // Format time
    function formatTime(seconds) {
      const mins = Math.floor(seconds / 60);
      const secs = Math.floor(seconds % 60);
      return mins + ':' + (secs < 10 ? '0' : '') + secs;
    }

    // Update waveform progress
    function updateWaveform(progress) {
      const activeCount = Math.floor(progress * waveformBars.length);
      waveformBars.forEach((bar, index) => {
        if (index < activeCount) {
          bar.classList.add('active');
        } else {
          bar.classList.remove('active');
        }
      });
    }

    // Play/Pause
    playBtn.addEventListener('click', () => {
      // Pause all other audio
      document.querySelectorAll('.audio-player audio').forEach(a => {
        if (a !== audio && !a.paused) {
          a.pause();
          const otherPlayer = a.closest('.audio-player');
          otherPlayer.querySelector('.play-icon').style.display = 'block';
          otherPlayer.querySelector('.pause-icon').style.display = 'none';
          otherPlayer.querySelector('.play-btn').classList.remove('playing');
        }
      });

      if (audio.paused) {
        audio.play();
        playIcon.style.display = 'none';
        pauseIcon.style.display = 'block';
        playBtn.classList.add('playing');
      } else {
        audio.pause();
        playIcon.style.display = 'block';
        pauseIcon.style.display = 'none';
        playBtn.classList.remove('playing');
      }
    });

    // Time update
    audio.addEventListener('timeupdate', () => {
      const progress = audio.currentTime / audio.duration;
      updateWaveform(progress);
      timeDisplay.textContent = formatTime(audio.currentTime);
    });

    // When audio ends
    audio.addEventListener('ended', () => {
      playIcon.style.display = 'block';
      pauseIcon.style.display = 'none';
      playBtn.classList.remove('playing');
      updateWaveform(0);
      timeDisplay.textContent = formatTime(0);
    });

    // Seek on waveform click
    waveformContainer.addEventListener('click', (e) => {
      const rect = waveformContainer.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const progress = clickX / rect.width;
      audio.currentTime = progress * audio.duration;
    });

    // Show duration when loaded
    audio.addEventListener('loadedmetadata', () => {
      timeDisplay.textContent = formatTime(0);
    });
  });
})();
</script>

'''

# Find the location to insert CSS (before </style></head>)
# Look for the last </style></head> occurrence
style_end = content.find('.curriculum_freelesson-wrapper {')
if style_end != -1:
    # Find the closing brace for this rule
    brace_count = 0
    i = style_end
    while i < len(content):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                # Insert CSS after this closing brace
                insert_pos = i + 1
                content = content[:insert_pos] + css_code + content[insert_pos:]
                print(f"CSS injected after .curriculum_freelesson-wrapper rule")
                break
        i += 1
else:
    print("Could not find .curriculum_freelesson-wrapper, trying alternate location")
    # Find </style></head> and insert before it
    style_head_pos = content.find('</style></head>')
    if style_head_pos != -1:
        content = content[:style_head_pos] + css_code + content[style_head_pos:]
        print("CSS injected before </style></head>")

# Find location to insert HTML (after curriculum section, before success section)
# Look for: </section><section class="section_success">
curriculum_end = content.find('<div id="curri" class="curriculum-anchor-link"></div></section>')
if curriculum_end != -1:
    insert_pos = curriculum_end + len('<div id="curri" class="curriculum-anchor-link"></div></section>')
    content = content[:insert_pos] + html_section + content[insert_pos:]
    print("HTML section injected after curriculum section")
else:
    print("Could not find curriculum section end marker")

# Find location to insert JavaScript (before </body>)
body_end = content.rfind('</body>')
if body_end != -1:
    content = content[:body_end] + js_code + content[body_end:]
    print("JavaScript injected before </body>")
else:
    print("Could not find </body>")

# Write the modified content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! Audio comparison section has been added.")
print("\nRemember to add these audio files to assets/audio/:")
print("  - singer-before.mp3")
print("  - singer-after.mp3")
print("  - rap-before.mp3")
print("  - rap-after.mp3")
