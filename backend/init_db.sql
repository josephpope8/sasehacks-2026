-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- Create Caretakers Table
create table if not exists public.caretakers (
  id uuid primary key default uuid_generate_v4(),
  first_name text not null,
  last_name text not null,
  email text unique not null,
  phone_number text not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Create Patients Table (We add a foreign key to caretakers)
create table if not exists public.patients (
  id uuid primary key default uuid_generate_v4(),
  first_name text not null,
  last_name text not null,
  phone_number text not null,
  timezone text not null,
  caretaker_id uuid references public.caretakers(id) on delete set null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Note: If public.patients already exists, the caretaker_id might not have a foreign key. 
-- Run this alter table if patients already existed:
-- alter table public.patients add constraint fk_caretaker foreign key (caretaker_id) references public.caretakers(id) on delete set null;

-- Create Medications Table
create table if not exists public.medications (
  id uuid primary key default uuid_generate_v4(),
  patient_id uuid references public.patients(id) on delete cascade not null,
  name text not null,
  dosage text not null,
  time_to_take text not null, -- Stored as 'HH:MM:SS'
  is_active boolean default true not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Create Medication Logs Table
create table if not exists public.medication_logs (
  id uuid primary key default uuid_generate_v4(),
  medication_id uuid references public.medications(id) on delete cascade not null,
  patient_id uuid references public.patients(id) on delete cascade not null,
  taken_at timestamp with time zone,
  status text not null, -- 'taken', 'missed', 'pending'
  scheduled_for timestamp with time zone not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Create Daily Checkups Table
create table if not exists public.daily_checkups (
  id uuid primary key default uuid_generate_v4(),
  patient_id uuid references public.patients(id) on delete cascade not null,
  mood text not null,
  notes text,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Create Reminders Table
create table if not exists public.reminders (
  id uuid primary key default uuid_generate_v4(),
  patient_id uuid references public.patients(id) on delete cascade not null,
  title text not null,
  description text,
  time_to_remind timestamp with time zone not null,
  is_active boolean default true not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
