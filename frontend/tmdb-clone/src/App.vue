<template>
  <div class="min-h-screen bg-background text-foreground">
    <!-- Navigation -->
    <nav class="p-4 flex items-center justify-between">
      <div class="text-primary font-bold text-2xl">TMDB</div>
      <div class="hidden md:flex space-x-6">
        <Button variant="ghost" v-for="item in navItems" :key="item">{{ item }}</Button>
      </div>
      <Button variant="outline" class="md:hidden">
        <Menu class="h-4 w-4" />
      </Button>
    </nav>

    <!-- Tab Navigation -->
    <div class="border-b border-border">
      <ScrollArea class="w-full whitespace-nowrap">
        <div class="flex space-x-6 px-4">
          <Button v-for="tab in tabs" :key="tab" variant="ghost" :class="{ 'border-b-2 border-primary': tab === 'Overview' }">
            {{ tab }}
          </Button>
        </div>
      </ScrollArea>
    </div>

    <!-- Hero Section -->
    <div v-if="movie" class="relative">
      <div class="bg-background/90">
        <div class="container mx-auto px-4 py-8">
          <div class="flex flex-col md:flex-row gap-8">
            <!-- Poster -->
            <div class="w-full md:w-1/3 lg:w-1/4">
              <img
                :src="movie.Poster"
                :alt="movie.Title"
                class="rounded-lg w-full shadow-lg"
              />
            </div>

            <!-- Content -->
            <div class="flex-1">
              <h1 class="text-4xl font-bold mb-2">
                {{ movie.Title }} ({{ movie.Year }})
              </h1>

              <div class="flex items-center gap-4 mb-6 flex-wrap">
                <Badge variant="secondary">{{ movie.Rated }}</Badge>
                <span>{{ movie.Runtime }}</span>
                <span>{{ movie.Genre }}</span>
              </div>

              <!-- Score and Actions -->
              <div class="flex items-center gap-6 mb-8 flex-wrap">
                <div class="flex items-center gap-2">
                  <Progress :value="userScore" class="w-16 h-16" />
                  <span class="font-medium">User Score</span>
                </div>

                <div class="flex gap-4">
                  <Button variant="outline" size="icon">
                    <Heart class="h-4 w-4" />
                  </Button>
                  <Button variant="outline" size="icon">
                    <Bookmark class="h-4 w-4" />
                  </Button>
                  <Button variant="outline" size="icon">
                    <Star class="h-4 w-4" />
                  </Button>
                </div>

                <Button class="hidden md:flex">
                  <PlayCircle class="mr-2 h-4 w-4" /> Play Trailer
                </Button>
              </div>

              <!-- Overview -->
              <div class="mb-8">
                <h2 class="text-2xl font-medium mb-2">Overview</h2>
                <p class="text-muted-foreground">{{ movie.Plot }}</p>
              </div>

              <!-- Credits -->
              <div class="grid grid-cols-2 md:grid-cols-3 gap-8">
                <div v-for="(credit, index) in credits" :key="index">
                  <h3 class="font-medium">{{ credit.name }}</h3>
                  <p class="text-muted-foreground">{{ credit.role }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Progress } from '@/components/ui/progress'
import { Menu, Heart, Bookmark, Star, PlayCircle } from 'lucide-vue-next'

const movie = ref(null)
const credits = ref([
  { name: 'James Gunn', role: 'Director, Writer' },
  { name: 'Stan Lee', role: 'Characters' },
  { name: 'Steve Gan', role: 'Characters' }
])

const navItems = ['Movies', 'TV Shows', 'People', 'More']
const tabs = ['Overview', 'Media', 'Fandom', 'Share']

const userScore = computed(() => {
  return movie.value ? Math.round(parseFloat(movie.value.imdbRating) * 10) : 0
})

onMounted(async () => {
  try {
    const response = await fetch('http://www.omdbapi.com/?i=tt3896198&apikey=d2132124')
    movie.value = await response.json()
  } catch (error) {
    console.error('Error fetching movie data:', error)
  }
})
</script>
